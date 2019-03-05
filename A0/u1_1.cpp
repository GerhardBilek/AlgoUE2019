/*
Aufgabe #1: Raute zeichnen

Beschreibung:
Die Raute wird über einen Zweischrittprozess generiert.
Der obere und untere Teil werden separat aufgebaut.
Die append Methode findet Verwendung um die Strings zu erstellen.

Anmerkung:
Die Raute wird entsprechend der Vorgabe aufgebaut.
Der folgende Fehler wird zusätzlich ausgegeben und kann zum momentanen Zeitpunkt nicht erklärt werden.
libc++abi.dylib: terminating with uncaught exception of type std::length_error: basic_string
Abort trap: 6
*/

#include <iostream>
#include <string>
using namespace std;

int main()
{
    int number;
    std::cout << "Geben Sie die Seitelänge an: ";
    std::cin >> number;                         //einlesen von einem Befehl

    int center = number+1;
    string star;
    string centerline = star.append(number, '*');

    // Oberter Teil der Raut bis inkl. Center-Line:
    for (int i = 0; i <=number; i++)
    {
    int n = number-i;
    star = " ";
    star.append(n, ' ');
    star.append(i*2+1, '*');
    cout << star << endl;
    }
    // Unterer Teil der Raute:
    for (int i = 0; i <=number; i++)
    {
    star = " ";
    int n = number;
 
    star.append(i+1, ' ');
    star.append((2*n-2*i)-1, '*');
    cout << star << endl; 
    }

    return 0;
}