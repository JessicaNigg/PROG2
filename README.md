# README - Budget planer

## Ausgangslage
Wer kennt es nicht...am Ende des Monats ist das Konto auf 0 geschrumpft und man weiss nicht wieso? Da wäre eine Übersicht über alle Kosten sehr hilfreich, welche einem motiviert seine Ausgaben zu minimieren, um auch nur einen kleinen Betrag auf sein Sparkonto übertragen zu können. Dies betrifft mich vor allem seit dem ich eine eigene Wohnung habe und nicht mehr 100% arbeite.

## Funktion/Projektidee
Die Idee ist ein Budgetplaner, der einem eine Übersicht über die monatlichen Kosten & Einnahmen gibt, sowie einem anzeigt, welchen Betrag man am Ende des Monats auf sein Sparkonto überweisen kann.

## Workflow
Die genauen Funktionen und den Datenstrom durch das Programm wird nachfolgend detailliert beschrieben.

### Dateneingabe
Man kann auf der Startseite einen neuen Monat erfassen, einen bestehenden Monat anzeigen lassen oder ihn auch komplett löschen. Ausserdem können Kosten und Einnahmen erfasst werden, welche angefallen sind.
In der Übersichtsseite können dann auch die bereits erfassten Kosten oder Einnahmen bearbeitet oder gelöscht werden.

### Datenverarbeitung/Speicherung
Diese Daten werden dann gespeichert und es wird der Betrag berechnet, welcher am Ende des Monats noch übrig bleibt. Diese veränderten Daten sollen dann ebenfalls gespeichert werden und für die Ausgabe zur Verfügung stehen.

### Datenausgabe
Als Ausgabe soll ein übersichtlicher Monatsüberblick erstellt werden, welcher dann ausgedruckt oder per Email versendet werden kann, um dann idealerweise den Endbetrag auf sein Sparkonto zu übertragen.

![Ablaufdiagramm](docs/bilder/Workflow_3.jpg)