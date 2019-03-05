/*
Excercise 3: Textumkehr - Drehen der Wörter in einem Satz

Ansatz:
String wird via User-Eingabe übergeben und in lowercase konvertiert.
Der String wird anhand von Leerzeichen zerlegt und jedes Wort in einem Array abgelegt.
Der erste Buchstabe wird extrahiert und in einen Großbustaben konvertiert.
Durch alternierender Ausgabe des Großbustaben und des restlichen Wortes wird der Satz ausgegeben.
*/

#include <iostream>
#include <string>
#include <sstream>
#include <cstring>
#include <vector>
#include <iterator>
using namespace std;

int main()
{
    cout << "Geben Sie einen Text ein: ";
    //string text = "David Hasselhoff redet mit seinem Auto"; // Teststring
    string text;
    getline (cin,text); // Ein Text mit Leerzeichen wird eingelesen

    // convert to lower case:
    for (int i= 0; i<=text.length(); i++)
        {
        text[i] = tolower(text[i]);
        }
    
    // Trennung des Satzes nach Leerzeichen und Speichern in Array:    
    std::istringstream iss(text);
    std::vector<std::string> results((std::istream_iterator<std::string>(iss)),(std::istream_iterator<std::string>()));

    // Der Array wird Wort für Wort ausgelesen
    int wörter = results.size();
    for (int w=0; w<wörter; w++)    // Warum funktioniert die Schleife nicht mit w=wörter?
    {
    string wort = results[w];     
        // Wort umdrehen:
        string xx = "";
        for (int i=wort.size();i>=0;i--){
            xx=xx+wort[i];
            
        }   
        string wort1 = xx;                   // Variable für das umgedrehte Wort.
        wort = xx;
        wort =toupper(wort[1]);              // Extraktion vom Großbuchstaben
        cout << wort;                        // Ausgabe des Großbustabens
        cout << wort1.substr(2) << " ";      //Ausgabe des erste ab der 2. Stelle (?) Warum die 2. Stelle
    }  
    return 0;
}

/*
//Versuche, Kontrolle und alternative Ansätze:


    // find space: 
    for (int i=0; i < text.size(); i++)
        if (text[i] == ' ' )   //wichtig: ' ' ist nicht " " 
        cout << "leer";
        else
        {
           cout << "nicht leer" << endl;
        }

    // Drucken der Results
    //for (int i=0; i<results.size();i++)
    //    cout << results[i] << " " << endl;

*/