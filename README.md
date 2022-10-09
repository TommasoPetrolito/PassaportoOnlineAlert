# PassaportoOnlineAlert
Questo repository contiene piccoli e semplici script python volti ad aiutare chi si trovi a dover prenotare un appuntamento su Passaporto Online (Passaporto Elettronico https://www.passaportonline.poliziadistato.it)


- gr.py è un semplice script che consente di ricevere una notifica qualora la pagina https://www.passaportonline.poliziadistato.it/GestioneDisponibilitaAction.do?codop=getDisponibilitaCittadino smetta di mostrare il messaggio "Non ci sono date disponibili" dal box con id "message_box_xl_dispo".


Questo script è utile in una situazione "normale" in cui non c'è disponibilità di date per la prenotazione e sostanzialmente vi avvertirà qualora improvvisamente "qualcosa cambiasse" e una data diventasse disponibile.


# PROVINCIA DI TORINO

Alla data del 09/10/2022, per quanto riguarda la Provincia di Torino, purtroppo la situazione è invece "anomala" ossia il sito presenta SEMPRE delle disponibilità nelle seguenti date:
- 06/03/2023
- 07/03/2023
- 08/03/2023
- 13/03/2023
- 29/03/2023
- 03/04/2023
- 05/04/2023


Dunque uno script aggiornato per questa situazione è in corso di sviluppo. 
