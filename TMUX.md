| Comando                 | Descrizione                                       |
| ----------------------- | ------------------------------------------------- |
| `tmux new -s nome`      | Crea una nuova sessione con nome​                 |
| `tmux ls`               | Elenca tutte le sessioni attive                   |
| `tmux a -t nome`        | Si riattacca (attach) a una sessione esistente    |
| `tmux kill-ses -t nome` | Elimina una sessione specifica                    |
| `tmux kill-ses -a`      | Elimina tutte le sessioni tranne quella corrente​ |

### Gestione Finestre
| Comando              | Descrizione                                 |
| -------------------- | ------------------------------------------- |
| `Ctrl+b` → `d`       | Detach: esci dalla sessione senza chiuderla |
| `Ctrl+b` → `$`       | Rinomina la sessione corrente               |
| `Ctrl+b` → `s`       | Mostra l'elenco interattivo delle sessioni  |
| `Ctrl+b` → `(` / `)` | Passa alla sessione precedente/successiva​  |
| `Ctrl+b` → `c`       | Crea una nuova finestra​                    |
| `Ctrl+b` → `,`       | Rinomina la finestra corrente​              |
| `Ctrl+b` → `w`       | Lista interattiva di tutte le finestre​     |
| `Ctrl+b` → `n` / `p` | Vai alla finestra successiva/precedente​    |
| `Ctrl+b` → `0`…`9`   | Vai alla finestra con quel numero​          |
| `Ctrl+b` → `l`       | Torna all'ultima finestra usata​            |
| `Ctrl+b` → `&`       | Chiudi la finestra corrente (con conferma)​ |
| `Ctrl+b` → `.`       | Sposta/rinumera la finestra​                |
| `Ctrl+b` → `f`       | Cerca una finestra per nome​                |

### Gestione Pannelli
| Comando                  | Descrizione                                    |
| ------------------------ | ---------------------------------------------- |
| `Ctrl+b` → `"`           | Split orizzontale (sopra/sotto)​               |
| `Ctrl+b` → `%`           | Split verticale (sinistra/destra)​             |
| `Ctrl+b` → `frecce`      | Naviga tra i pannelli​                         |
| `Ctrl+b` → `x`           | Chiudi il pannello corrente​                   |
| `Ctrl+b` → `z`           | Toggle fullscreen del pannello corrente​       |
| `Ctrl+b` → `{` / `}`     | Sposta il pannello a sinistra/destra​          |
| `Ctrl+b` → `o`           | Passa al pannello successivo​                  |
| `Ctrl+b` → `;`           | Torna all'ultimo pannello usato​               |
| `Ctrl+b` → `q`           | Mostra i numeri dei pannelli​                  |
| `Ctrl+b` → `q` → `0`…`9` | Vai al pannello con quel numero​               |
| `Ctrl+b` → `!`           | Converti il pannello in una finestra separata​ |
| `Ctrl+b` → `Space`       | Cicla tra i layout predefiniti​                |

### Comandi Utili
| Comando                         | Descrizione                                      |
| ------------------------------- | ------------------------------------------------ |
| `Ctrl+b` → `?`                  | Mostra TUTTI gli shortcut disponibili quickref+1 |
| `Ctrl+b` → `:`                  | Entra in command mode (per comandi avanzati)​    |
| `Ctrl+b` → `t`                  | Mostra un orologio nel pannello​                 |
| `tmux source-file ~/.tmux.conf` | Ricarica la configurazione​                      |
##### CONFIGS:
Per impostare le regole in tmux, scriverle in `~/.tmux.conf`.

```
set -g mouse on
```

Salvare le regole o ripristinarle con `tmux source-file ~/.tmux.conf`