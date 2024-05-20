
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = '2DUP AT CHAR CR DEFINED_WORD DIVIDE DO DOT DROP DUP ELSE EMIT EQUALS EXCLAMATION IF INFEQ INFERIOR INT KEY LOOP MINUS MOD NAME PLUS SEMICOLON SPACE SPACES STRING SUPEQ SUPERIOR SWAP THEN TIMES VARIABLEinicio : ComandosComandos : Comando Comandos\n                | ComandoComando : Valores\n               | Operadores \n               | Declaracao\n               | Print\n               | Operacao\n               | Condicional\n               | Ciclo\n               | DEFINED_WORD\n    Condicional : IF Comandos ELSE Comandos THEN\n                   | IF Comandos ELSE THEN\n                   | IF Comandos THEN\n                   | IF THENCiclo : DO Comandos LOOPOperacao : KEY\n                | DUP\n                | 2DUP\n                | SWAP\n                | DROPPrint : STRING\n             | EMIT\n             | DOT\n             | CHAR\n             | SPACE\n             | SPACES\n             | CRValores : INTDeclaracao : DeclaracaoF\n                  | DeclaracaoVDeclaracaoF : NAME Comandos SEMICOLONDeclaracaoV : VARIABLE\n                   | EXCLAMATION\n                   | ATOperadores :  PLUS\n                    | MINUS\n                    | TIMES\n                    | DIVIDE\n                    | MOD\n                    | SUPEQ\n                    | INFEQ\n                    | INFERIOR\n                    | SUPERIOR\n                    | EQUALS\n        '
    
_lr_action_items = {'DEFINED_WORD':([0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,45,48,49,50,51,53,54,],[11,11,-4,-5,-6,-7,-8,-9,-10,-11,-29,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-30,-31,-22,-23,-24,-25,-26,-27,-28,-17,-18,-19,-20,-21,11,11,11,-33,-34,-35,-15,11,-14,-16,-32,-13,-12,]),'INT':([0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,45,48,49,50,51,53,54,],[12,12,-4,-5,-6,-7,-8,-9,-10,-11,-29,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-30,-31,-22,-23,-24,-25,-26,-27,-28,-17,-18,-19,-20,-21,12,12,12,-33,-34,-35,-15,12,-14,-16,-32,-13,-12,]),'PLUS':([0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,45,48,49,50,51,53,54,],[13,13,-4,-5,-6,-7,-8,-9,-10,-11,-29,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-30,-31,-22,-23,-24,-25,-26,-27,-28,-17,-18,-19,-20,-21,13,13,13,-33,-34,-35,-15,13,-14,-16,-32,-13,-12,]),'MINUS':([0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,45,48,49,50,51,53,54,],[14,14,-4,-5,-6,-7,-8,-9,-10,-11,-29,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-30,-31,-22,-23,-24,-25,-26,-27,-28,-17,-18,-19,-20,-21,14,14,14,-33,-34,-35,-15,14,-14,-16,-32,-13,-12,]),'TIMES':([0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,45,48,49,50,51,53,54,],[15,15,-4,-5,-6,-7,-8,-9,-10,-11,-29,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-30,-31,-22,-23,-24,-25,-26,-27,-28,-17,-18,-19,-20,-21,15,15,15,-33,-34,-35,-15,15,-14,-16,-32,-13,-12,]),'DIVIDE':([0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,45,48,49,50,51,53,54,],[16,16,-4,-5,-6,-7,-8,-9,-10,-11,-29,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-30,-31,-22,-23,-24,-25,-26,-27,-28,-17,-18,-19,-20,-21,16,16,16,-33,-34,-35,-15,16,-14,-16,-32,-13,-12,]),'MOD':([0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,45,48,49,50,51,53,54,],[17,17,-4,-5,-6,-7,-8,-9,-10,-11,-29,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-30,-31,-22,-23,-24,-25,-26,-27,-28,-17,-18,-19,-20,-21,17,17,17,-33,-34,-35,-15,17,-14,-16,-32,-13,-12,]),'SUPEQ':([0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,45,48,49,50,51,53,54,],[18,18,-4,-5,-6,-7,-8,-9,-10,-11,-29,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-30,-31,-22,-23,-24,-25,-26,-27,-28,-17,-18,-19,-20,-21,18,18,18,-33,-34,-35,-15,18,-14,-16,-32,-13,-12,]),'INFEQ':([0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,45,48,49,50,51,53,54,],[19,19,-4,-5,-6,-7,-8,-9,-10,-11,-29,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-30,-31,-22,-23,-24,-25,-26,-27,-28,-17,-18,-19,-20,-21,19,19,19,-33,-34,-35,-15,19,-14,-16,-32,-13,-12,]),'INFERIOR':([0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,45,48,49,50,51,53,54,],[20,20,-4,-5,-6,-7,-8,-9,-10,-11,-29,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-30,-31,-22,-23,-24,-25,-26,-27,-28,-17,-18,-19,-20,-21,20,20,20,-33,-34,-35,-15,20,-14,-16,-32,-13,-12,]),'SUPERIOR':([0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,45,48,49,50,51,53,54,],[21,21,-4,-5,-6,-7,-8,-9,-10,-11,-29,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-30,-31,-22,-23,-24,-25,-26,-27,-28,-17,-18,-19,-20,-21,21,21,21,-33,-34,-35,-15,21,-14,-16,-32,-13,-12,]),'EQUALS':([0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,45,48,49,50,51,53,54,],[22,22,-4,-5,-6,-7,-8,-9,-10,-11,-29,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-30,-31,-22,-23,-24,-25,-26,-27,-28,-17,-18,-19,-20,-21,22,22,22,-33,-34,-35,-15,22,-14,-16,-32,-13,-12,]),'STRING':([0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,45,48,49,50,51,53,54,],[25,25,-4,-5,-6,-7,-8,-9,-10,-11,-29,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-30,-31,-22,-23,-24,-25,-26,-27,-28,-17,-18,-19,-20,-21,25,25,25,-33,-34,-35,-15,25,-14,-16,-32,-13,-12,]),'EMIT':([0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,45,48,49,50,51,53,54,],[26,26,-4,-5,-6,-7,-8,-9,-10,-11,-29,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-30,-31,-22,-23,-24,-25,-26,-27,-28,-17,-18,-19,-20,-21,26,26,26,-33,-34,-35,-15,26,-14,-16,-32,-13,-12,]),'DOT':([0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,45,48,49,50,51,53,54,],[27,27,-4,-5,-6,-7,-8,-9,-10,-11,-29,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-30,-31,-22,-23,-24,-25,-26,-27,-28,-17,-18,-19,-20,-21,27,27,27,-33,-34,-35,-15,27,-14,-16,-32,-13,-12,]),'CHAR':([0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,45,48,49,50,51,53,54,],[28,28,-4,-5,-6,-7,-8,-9,-10,-11,-29,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-30,-31,-22,-23,-24,-25,-26,-27,-28,-17,-18,-19,-20,-21,28,28,28,-33,-34,-35,-15,28,-14,-16,-32,-13,-12,]),'SPACE':([0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,45,48,49,50,51,53,54,],[29,29,-4,-5,-6,-7,-8,-9,-10,-11,-29,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-30,-31,-22,-23,-24,-25,-26,-27,-28,-17,-18,-19,-20,-21,29,29,29,-33,-34,-35,-15,29,-14,-16,-32,-13,-12,]),'SPACES':([0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,45,48,49,50,51,53,54,],[30,30,-4,-5,-6,-7,-8,-9,-10,-11,-29,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-30,-31,-22,-23,-24,-25,-26,-27,-28,-17,-18,-19,-20,-21,30,30,30,-33,-34,-35,-15,30,-14,-16,-32,-13,-12,]),'CR':([0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,45,48,49,50,51,53,54,],[31,31,-4,-5,-6,-7,-8,-9,-10,-11,-29,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-30,-31,-22,-23,-24,-25,-26,-27,-28,-17,-18,-19,-20,-21,31,31,31,-33,-34,-35,-15,31,-14,-16,-32,-13,-12,]),'KEY':([0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,45,48,49,50,51,53,54,],[32,32,-4,-5,-6,-7,-8,-9,-10,-11,-29,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-30,-31,-22,-23,-24,-25,-26,-27,-28,-17,-18,-19,-20,-21,32,32,32,-33,-34,-35,-15,32,-14,-16,-32,-13,-12,]),'DUP':([0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,45,48,49,50,51,53,54,],[33,33,-4,-5,-6,-7,-8,-9,-10,-11,-29,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-30,-31,-22,-23,-24,-25,-26,-27,-28,-17,-18,-19,-20,-21,33,33,33,-33,-34,-35,-15,33,-14,-16,-32,-13,-12,]),'2DUP':([0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,45,48,49,50,51,53,54,],[34,34,-4,-5,-6,-7,-8,-9,-10,-11,-29,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-30,-31,-22,-23,-24,-25,-26,-27,-28,-17,-18,-19,-20,-21,34,34,34,-33,-34,-35,-15,34,-14,-16,-32,-13,-12,]),'SWAP':([0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,45,48,49,50,51,53,54,],[35,35,-4,-5,-6,-7,-8,-9,-10,-11,-29,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-30,-31,-22,-23,-24,-25,-26,-27,-28,-17,-18,-19,-20,-21,35,35,35,-33,-34,-35,-15,35,-14,-16,-32,-13,-12,]),'DROP':([0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,45,48,49,50,51,53,54,],[36,36,-4,-5,-6,-7,-8,-9,-10,-11,-29,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-30,-31,-22,-23,-24,-25,-26,-27,-28,-17,-18,-19,-20,-21,36,36,36,-33,-34,-35,-15,36,-14,-16,-32,-13,-12,]),'IF':([0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,45,48,49,50,51,53,54,],[37,37,-4,-5,-6,-7,-8,-9,-10,-11,-29,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-30,-31,-22,-23,-24,-25,-26,-27,-28,-17,-18,-19,-20,-21,37,37,37,-33,-34,-35,-15,37,-14,-16,-32,-13,-12,]),'DO':([0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,45,48,49,50,51,53,54,],[38,38,-4,-5,-6,-7,-8,-9,-10,-11,-29,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-30,-31,-22,-23,-24,-25,-26,-27,-28,-17,-18,-19,-20,-21,38,38,38,-33,-34,-35,-15,38,-14,-16,-32,-13,-12,]),'NAME':([0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,45,48,49,50,51,53,54,],[39,39,-4,-5,-6,-7,-8,-9,-10,-11,-29,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-30,-31,-22,-23,-24,-25,-26,-27,-28,-17,-18,-19,-20,-21,39,39,39,-33,-34,-35,-15,39,-14,-16,-32,-13,-12,]),'VARIABLE':([0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,45,48,49,50,51,53,54,],[40,40,-4,-5,-6,-7,-8,-9,-10,-11,-29,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-30,-31,-22,-23,-24,-25,-26,-27,-28,-17,-18,-19,-20,-21,40,40,40,-33,-34,-35,-15,40,-14,-16,-32,-13,-12,]),'EXCLAMATION':([0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,45,48,49,50,51,53,54,],[41,41,-4,-5,-6,-7,-8,-9,-10,-11,-29,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-30,-31,-22,-23,-24,-25,-26,-27,-28,-17,-18,-19,-20,-21,41,41,41,-33,-34,-35,-15,41,-14,-16,-32,-13,-12,]),'AT':([0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,45,48,49,50,51,53,54,],[42,42,-4,-5,-6,-7,-8,-9,-10,-11,-29,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-30,-31,-22,-23,-24,-25,-26,-27,-28,-17,-18,-19,-20,-21,42,42,42,-33,-34,-35,-15,42,-14,-16,-32,-13,-12,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,40,41,42,43,45,49,50,51,53,54,],[0,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-29,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-30,-31,-22,-23,-24,-25,-26,-27,-28,-17,-18,-19,-20,-21,-33,-34,-35,-2,-15,-14,-16,-32,-13,-12,]),'ELSE':([3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,40,41,42,43,44,45,49,50,51,53,54,],[-3,-4,-5,-6,-7,-8,-9,-10,-11,-29,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-30,-31,-22,-23,-24,-25,-26,-27,-28,-17,-18,-19,-20,-21,-33,-34,-35,-2,48,-15,-14,-16,-32,-13,-12,]),'THEN':([3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,40,41,42,43,44,45,48,49,50,51,52,53,54,],[-3,-4,-5,-6,-7,-8,-9,-10,-11,-29,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-30,-31,-22,-23,-24,-25,-26,-27,-28,-17,-18,-19,-20,-21,45,-33,-34,-35,-2,49,-15,53,-14,-16,-32,54,-13,-12,]),'LOOP':([3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,40,41,42,43,45,46,49,50,51,53,54,],[-3,-4,-5,-6,-7,-8,-9,-10,-11,-29,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-30,-31,-22,-23,-24,-25,-26,-27,-28,-17,-18,-19,-20,-21,-33,-34,-35,-2,-15,50,-14,-16,-32,-13,-12,]),'SEMICOLON':([3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,40,41,42,43,45,47,49,50,51,53,54,],[-3,-4,-5,-6,-7,-8,-9,-10,-11,-29,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-30,-31,-22,-23,-24,-25,-26,-27,-28,-17,-18,-19,-20,-21,-33,-34,-35,-2,-15,51,-14,-16,-32,-13,-12,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'inicio':([0,],[1,]),'Comandos':([0,3,37,38,39,48,],[2,43,44,46,47,52,]),'Comando':([0,3,37,38,39,48,],[3,3,3,3,3,3,]),'Valores':([0,3,37,38,39,48,],[4,4,4,4,4,4,]),'Operadores':([0,3,37,38,39,48,],[5,5,5,5,5,5,]),'Declaracao':([0,3,37,38,39,48,],[6,6,6,6,6,6,]),'Print':([0,3,37,38,39,48,],[7,7,7,7,7,7,]),'Operacao':([0,3,37,38,39,48,],[8,8,8,8,8,8,]),'Condicional':([0,3,37,38,39,48,],[9,9,9,9,9,9,]),'Ciclo':([0,3,37,38,39,48,],[10,10,10,10,10,10,]),'DeclaracaoF':([0,3,37,38,39,48,],[23,23,23,23,23,23,]),'DeclaracaoV':([0,3,37,38,39,48,],[24,24,24,24,24,24,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> inicio","S'",1,None,None,None),
  ('inicio -> Comandos','inicio',1,'p_inicio','gramatica.py',8),
  ('Comandos -> Comando Comandos','Comandos',2,'p_Comandos','gramatica.py',12),
  ('Comandos -> Comando','Comandos',1,'p_Comandos','gramatica.py',13),
  ('Comando -> Valores','Comando',1,'p_Comando','gramatica.py',22),
  ('Comando -> Operadores','Comando',1,'p_Comando','gramatica.py',23),
  ('Comando -> Declaracao','Comando',1,'p_Comando','gramatica.py',24),
  ('Comando -> Print','Comando',1,'p_Comando','gramatica.py',25),
  ('Comando -> Operacao','Comando',1,'p_Comando','gramatica.py',26),
  ('Comando -> Condicional','Comando',1,'p_Comando','gramatica.py',27),
  ('Comando -> Ciclo','Comando',1,'p_Comando','gramatica.py',28),
  ('Comando -> DEFINED_WORD','Comando',1,'p_Comando','gramatica.py',29),
  ('Condicional -> IF Comandos ELSE Comandos THEN','Condicional',5,'p_Condicional','gramatica.py',35),
  ('Condicional -> IF Comandos ELSE THEN','Condicional',4,'p_Condicional','gramatica.py',36),
  ('Condicional -> IF Comandos THEN','Condicional',3,'p_Condicional','gramatica.py',37),
  ('Condicional -> IF THEN','Condicional',2,'p_Condicional','gramatica.py',38),
  ('Ciclo -> DO Comandos LOOP','Ciclo',3,'p_Ciclo','gramatica.py',53),
  ('Operacao -> KEY','Operacao',1,'p_Operacao','gramatica.py',59),
  ('Operacao -> DUP','Operacao',1,'p_Operacao','gramatica.py',60),
  ('Operacao -> 2DUP','Operacao',1,'p_Operacao','gramatica.py',61),
  ('Operacao -> SWAP','Operacao',1,'p_Operacao','gramatica.py',62),
  ('Operacao -> DROP','Operacao',1,'p_Operacao','gramatica.py',63),
  ('Print -> STRING','Print',1,'p_Print','gramatica.py',67),
  ('Print -> EMIT','Print',1,'p_Print','gramatica.py',68),
  ('Print -> DOT','Print',1,'p_Print','gramatica.py',69),
  ('Print -> CHAR','Print',1,'p_Print','gramatica.py',70),
  ('Print -> SPACE','Print',1,'p_Print','gramatica.py',71),
  ('Print -> SPACES','Print',1,'p_Print','gramatica.py',72),
  ('Print -> CR','Print',1,'p_Print','gramatica.py',73),
  ('Valores -> INT','Valores',1,'p_Valores','gramatica.py',77),
  ('Declaracao -> DeclaracaoF','Declaracao',1,'p_Declaracao','gramatica.py',82),
  ('Declaracao -> DeclaracaoV','Declaracao',1,'p_Declaracao','gramatica.py',83),
  ('DeclaracaoF -> NAME Comandos SEMICOLON','DeclaracaoF',3,'p_DeclaracaoF','gramatica.py',88),
  ('DeclaracaoV -> VARIABLE','DeclaracaoV',1,'p_DeclaracaoV','gramatica.py',104),
  ('DeclaracaoV -> EXCLAMATION','DeclaracaoV',1,'p_DeclaracaoV','gramatica.py',105),
  ('DeclaracaoV -> AT','DeclaracaoV',1,'p_DeclaracaoV','gramatica.py',106),
  ('Operadores -> PLUS','Operadores',1,'p_Operadores','gramatica.py',111),
  ('Operadores -> MINUS','Operadores',1,'p_Operadores','gramatica.py',112),
  ('Operadores -> TIMES','Operadores',1,'p_Operadores','gramatica.py',113),
  ('Operadores -> DIVIDE','Operadores',1,'p_Operadores','gramatica.py',114),
  ('Operadores -> MOD','Operadores',1,'p_Operadores','gramatica.py',115),
  ('Operadores -> SUPEQ','Operadores',1,'p_Operadores','gramatica.py',116),
  ('Operadores -> INFEQ','Operadores',1,'p_Operadores','gramatica.py',117),
  ('Operadores -> INFERIOR','Operadores',1,'p_Operadores','gramatica.py',118),
  ('Operadores -> SUPERIOR','Operadores',1,'p_Operadores','gramatica.py',119),
  ('Operadores -> EQUALS','Operadores',1,'p_Operadores','gramatica.py',120),
]
