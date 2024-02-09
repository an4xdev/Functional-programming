gra(cyberpunk2077, singleplayer, trzyD, rpg, platna, bogata_fabula, duze).
gra(amongUs, multiplayer, dwaD, strategia, darmowa, poboczna_fabula, male).
gra(counterStrike, multiplayer, trzyD, fps, platna, poboczna_fabula, male).
gra(starcraft, singleplayer, dwaD, strategia, platna, bogata_fabula, male).
gra(witcher3, singleplayer, trzyD, rpg, platna, bogata_fabula, duze).
gra(minecraft, multiplayer, trzyD, sandbox, platna, poboczna_fabula, male).
gra(leagueOfLegends, multiplayer, trzyD, moba, darmowa, poboczna_fabula, male).
gra(terraria, singleplayer, dwaD, sandbox, platna, bogata_fabula, male).
gra(redDeadRedemption2, singleplayer, trzyD, akcja, platna, bogata_fabula, duze).
gra(fortnite, multiplayer, trzyD, battleRoyale, darmowa, poboczna_fabula, duze).
gra(overwatch, multiplayer, trzyD, fps, platna, poboczna_fabula, duze).
gra(theLastOfUsPartII, singleplayer, trzyD, przygodowa, platna, bogata_fabula, duze).
gra(rocketLeague, multiplayer, trzyD, sportowa, platna, poboczna_fabula, male).
gra(celeste, singleplayer, dwaD, platformowa, platna, bogata_fabula, male).
gra(skyrim, singleplayer, trzyD, rpg, platna, bogata_fabula, duze).
gra(apexLegends, multiplayer, trzyD, battleRoyale, darmowa, poboczna_fabula, duze).

podpowiedz :-
    write('Podaj tryb gry: m. multiplayer s. singleplayer d. dowolna '), read(TrybOdp),
    (TrybOdp == m -> Tryb = multiplayer; TrybOdp == s -> Tryb = singleplayer; Tryb = _),
    write('Podaj typ grafiki: d. 2D t. 3D x. dowolna'), read(GrafikaOdp),
    (GrafikaOdp == d -> Grafika = dwaD; GrafikaOdp == t -> Grafika = trzyD; Grafika = _),
    write('Podaj rodzaj gry: '), read(Rodzaj),
    write('Czy gra musi byc darmowa (tak/nie)? '), read(CenaOdp),
    (CenaOdp == tak -> Cena = darmowa; Cena = _),
    write('Czy zalezy Ci na fabule (tak/nie)? '), read(FabulaOdp),
    (FabulaOdp == tak -> Fabula = bogata_fabula; Fabula = _),
    write('Czy zalezy ci na niskich wymaganiach sprzetowych(tak/nie): '), read(WymaganiaOdp),
    (WymaganiaOdp == tak -> Wymagania = male; Wymagania = _),
    findall(Gra, gra(Gra, Tryb, Grafika, Rodzaj, Cena, Fabula, Wymagania), Gry),
    wypisz_gry(Gry).

wypisz_gry([]) :- write('Nie znaleziono pasujacych gier.'), nl.
wypisz_gry(Gry) :-
    write('Sugerowane gry: '), nl,
    wypisz_gry_lista(Gry).

wypisz_gry_lista([]).
wypisz_gry_lista([Gra|Reszta]) :-
    write(Gra), nl,
    wypisz_gry_lista(Reszta).

:-podpowiedz.