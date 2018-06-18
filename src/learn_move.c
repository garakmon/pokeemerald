// mostly taken from pokeruby so credit to camthesaxman
// includes
#include "global.h"
//#include "data2.h"
//#include "field_fadetransition.h"
//#include "main.h"
//#include "menu.h"
//#include "menu_cursor.h"
#include "palette.h" // TransferPlttBuffer(), BeginNormalPaletteFade(), 
//#include "pokemon.h"
//#include "rom4.h"
//#include "script.h" // ScriptContext2_Enable(), 
//#include "songs.h"
//#include "sound.h"
#include "sprite.h" // LoadOam(), ProcessSpriteCopyRequests()
//#include "string_util.h"
//#include "strings.h"
//#include "strings2.h"
//#include "task.h" // CreateTask
//#include "trig.h"

// forward declarations
//void sub_8160664(u8);

void sub_8160624(void)
{
    LoadOam();
    ProcessSpriteCopyRequests();
    TransferPlttBuffer();
}

/*void sub_8160638(void)
{
    ScriptContext2_Enable();
    CreateTask(sub_8160664, 10);
    BeginNormalPaletteFade(0xFFFFFFFF, 0, 0, 16, 0);
}*/


