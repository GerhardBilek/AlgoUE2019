/*     Excercise 2: Primzahlprüfung

Ansatz:
Die zu prüfende Zahl wird mittels for Loop durch alle potentiellen Zahlen dividiert.

Für die Teiler die 0 ergeben gitl:
-) Die Anzahl der Teiler wird in einer int Variable gespeichert.
-) Die Teiler selbst werden in einen String konvertiert und ebenfalls gespeichert.

Bei Primzahl: Es wird die Primzahl ausgegeben, wenn der Anzahl der der 0-Teiler gleich 0 ist.
Keine Primzahl: Die Teiler, die im String abgelegt sind, werden ausgegeben.

*/

#include <iostream>
using namespace std;

int main()
{
    // Eingabe der zu prüfenden Zahl
    cout  << "Geben Sie eine positive ganze Zahl ein: ";
    int numberCheck;
    cin >> numberCheck;
    
    // Speichervariablen:
    int NullReste = 0;          // Summieren der Teileranzahl, die 0 als Rest generieren
    string NullTeiler;          // String zur Ablage der Teiler, die 0 als Rest generieren
     
    // Durchführung der Divisionen um den Rest zu erhalten:
    for (int prim_teiler = 2; prim_teiler<numberCheck; prim_teiler++)
    {
        int Testresultat = numberCheck%prim_teiler;        // Modulo-Operator um den Rest zu erhalten.
        if (Testresultat == 0) {
            NullReste+=1;
            NullTeiler += to_string(prim_teiler);
            NullTeiler.append(" ");
        }  
    }

    // Ausgabe der Info ob es sich um eine Primzahl handelt & Teiler:
    if (NullReste == 0) cout << numberCheck << " ist eine Primzahl!" << endl;
    else cout << numberCheck <<  " ist keine Primzahl." << endl << "Teiler: " << NullTeiler;
    
return 0;
}

/*
____________________Entwürfe:

    int Teiler[numberCheck];
    int Teilerzähler = 0;

    else {    
            Teiler[Teilerzähler] = prim_teiler;
            Teilerzähler++;
        }

*/