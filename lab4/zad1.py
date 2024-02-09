from functools import partial


def is_spam_based_on_rules(msg, required, sufficient):
    meets_required = all(rule(msg) for rule in required)
    meets_sufficient = any(rule(msg) for rule in sufficient)
    return meets_required or meets_sufficient


def create_single_rule_spam_checker(rule_set):
    required, sufficient = rule_set
    return partial(is_spam_based_on_rules, required=required, sufficient=sufficient)


def create_spam_checker(rule_sets_list):
    checkers = [create_single_rule_spam_checker(
        rule_set) for rule_set in rule_sets_list]

    def combined_spam_checker(msg):
        return any(checker(msg) for checker in checkers)
    return combined_spam_checker


required_rules1 = (
    lambda msg: not any(char.isalpha() for char in msg),
    lambda msg: len(msg) > 15,
)
sufficient_rules1 = (
    lambda msg: "click here" in msg.lower(),
    lambda msg: "urgent action required" in msg.lower(),
)
required_rules2 = (
    lambda msg: "free" in msg.lower(),
    lambda msg: msg.count("!") > 2,
)
sufficient_rules2 = (
    lambda msg: "prize" in msg.lower(),
    lambda msg: "win" in msg.lower(),
)

spam_checker = create_spam_checker([
    (required_rules1, sufficient_rules1),
    (required_rules2, sufficient_rules2),
])

messages = [
    ("Alice", "Click here for a special offer!"),
    ("Bob", "Urgent action required: Confirm your email now."),
    ("Charlie", "Congratulations, dear customer! You're a winner of our lucky draw."),
    ("Alice", "!!! 😀😀😀😀😀😀 !!!"),
    ("Bob", "Hello, how are you doing?"),
    ("Charlie", "I'll call you tomorrow."),
    ("Alice", "Good day! Hope you're well."),
    ("Bob", "😀 Urgent action required 😀"),
    ("Charlie", "!!! 😃 Click here 😃 !!!"),
    ("Alice", "❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗"),
]


def check_messages_for_spam(messages, checker):
    spam_count_by_author = {}
    spam_messages = []
    for author, message in messages:
        if spam_count_by_author.get(author, 0) >= 3:
            spam_messages.append((author, message))
            continue
        if checker(message):
            spam_messages.append((author, message))
            spam_count_by_author[author] = spam_count_by_author.get(
                author, 0) + 1
    return spam_messages


spam_messages = check_messages_for_spam(messages, spam_checker)
print(spam_messages)
