# Server-ok? Labo 6
Dit is een network monitoring tool waarmee je aan de hand van een ping kunt nagaan of een server bereikbaar is of niet.

# Beschikbare commands
<ins>management</ins>: Opent het beheerdersmodus. U kunt de bestaande servers bekijken, toevoegen of verwijderen.

<ins>check</ins>: Controleert of de servers in de lijst bereikbaar zijn of niet. Dit wordt gedaan door de ping-opdracht naar elke server in de lijst uit te voeren en de status te rapporteren.

<ins>add {hostnaam of IP-adress}</ins>: Voegt een nieuwe server toe aan de lijst. Dit wordt gedaan door de hostnaam of IP-adress van de server als argument mee te geven aan de opdracht. Bijvoorbeeld: python main.py add example.com.

<ins>delete {lijstnummer}</ins>: Verwijdert een server uit de lijst. Dit wordt gedaan door het lijstnummer van de lijst als argument mee te geven aan de opdracht. Bijvoorbeeld: python main.py delete 2 verwijdert de tweede server uit de lijst.

<ins>list</ins>: Toont de lijst van servers die zijn opgeslagen.

<em>Note: De commands zijn allemaal in kleine letters.</em>
