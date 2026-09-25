import json
from pathlib import Path

PAGES_DIR = Path("cache/pages")
PAGES_DIR.mkdir(parents=True, exist_ok=True)

pages = {}

# Page 216
pages["page_216"] = {
    "page": "216",
    "file": "recetario _216.jpg",
    "model": "claude-3-7-sonnet",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "AMBROSIA SAUCE",
            "normalized_title": "ambrosia sauce",
            "is_continuation": False,
            "ingredients": [
                "1 Taza de piña triturada en su jugo",
                "1 Taza de gajos de mandarinas escurridas",
                "1/2 Taza de coco rallado",
                "2 Cdas. de azúcar",
                "1 Cda. de maicena",
                "2 Cdas. de jugo de naranja o agua",
                "1 Cdita. de jugo de limón"
            ],
            "steps": [
                "Disolver la maicena en las 2 cucharadas de jugo de naranja o agua.",
                "En una olla pequeña, combinar la piña triturada con su jugo, las mandarinas escurridas, el coco rallado y el azúcar.",
                "Agregar la maicena disuelta y el jugo de limón.",
                "Cocinar a fuego medio, revolviendo constantemente hasta que espese y rompa en hervor suave.",
                "Retirar del fuego y servir tibia o fría sobre pasteles, bizcochos o helado."
            ],
            "notes": [
                "Salsa frutal aromática para bañar postres o acompañar pasteles."
            ],
            "handwritten_notes": []
        },
        {
            "kind": "recipe",
            "title": "SALSA DE NARANJA",
            "normalized_title": "salsa de naranja",
            "is_continuation": False,
            "ingredients": [
                "1/2 Taza de azúcar",
                "1 Cda. de maicena",
                "1 Taza de jugo de naranja natural",
                "1 Cdita. de jugo de limón",
                "Ralladura de 1 naranja",
                "1 Cda. de mantequilla"
            ],
            "steps": [
                "En una cacerola pequeña, mezclar el azúcar y la maicena.",
                "Añadir gradualmente el jugo de naranja natural, el jugo de limón y la ralladura de naranja.",
                "Cocinar a fuego medio moviendo constantemente con batidor o cuchara hasta que hierva y tome consistencia espesa y transparente.",
                "Retirar del fuego e incorporar la mantequilla batiendo hasta derretir.",
                "Servir tibia sobre crepes, panqueques o queques."
            ],
            "notes": [],
            "handwritten_notes": []
        }
    ],
    "continues_next": False,
    "legibility": "good",
    "rotation_issue": False
}

# Page 217
pages["page_217"] = {
    "page": "217",
    "file": "recetario _217.jpg",
    "model": "claude-3-7-sonnet",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "PASTA BASICA PARA CREPES DULCES",
            "normalized_title": "pasta basica para crepes dulces",
            "is_continuation": False,
            "ingredients": [
                "1 Taza de harina cernida",
                "1/4 Cdita. de sal",
                "1 Cda. de azúcar",
                "3 Huevos ligeramente batidos",
                "1 1/2 Taza de leche",
                "2 Cdas. de mantequilla derretida"
            ],
            "steps": [
                "Cernir juntos la harina, la sal y el azúcar.",
                "Aparte batir ligeramente los huevos con la leche y la mantequilla derretida.",
                "Verter los líquidos poco a poco sobre los secos batiendo hasta que no queden grumos.",
                "Dejar reposar la masa en refrigeración durante 30 minutos.",
                "Calentar una sartén engrasada con mantequilla a fuego medio, verter una porción delgada extendiendo por el fondo; voltear y dorar ambos lados."
            ],
            "notes": [],
            "handwritten_notes": []
        },
        {
            "kind": "recipe",
            "title": "CREPES FLAMBEE",
            "normalized_title": "crepes flambee",
            "is_continuation": False,
            "ingredients": [
                "Crepes preparadas",
                "Mantequilla",
                "Azúcar",
                "Jugo de naranja natural",
                "Jugo de limón",
                "Licor de naranja (Grand Marnier o Cointreau)",
                "Ron para flambear"
            ],
            "steps": [
                "Derretir mantequilla en una sartén con azúcar, jugo de naranja y limón.",
                "Doblar las crepes en cuatro (triángulos) y disponer en la sartén para calentarlas y bañarlas en el almíbar.",
                "Agregar licor de naranja y ron tibio; flambear con precaución hasta que se apague la llama.",
                "Servir calientes inmediatamente."
            ],
            "notes": ["De origen polinesio."],
            "handwritten_notes": []
        },
        {
            "kind": "recipe",
            "title": "CREPES ENSUEÑO DE LIMON",
            "normalized_title": "crepes ensueno de limon",
            "is_continuation": False,
            "ingredients": [
                "Crepes preparadas",
                "1 1/2 Taza de azúcar",
                "Jugo de limón al gusto",
                "Ralladura de limón",
                "Mantequilla"
            ],
            "steps": [
                "Poner al fuego la mantequilla con azúcar, jugo de limón y ralladura hasta hacer un jarabe ligero.",
                "Pasar las crepes dobladas por el jarabe caliente.",
                "Servir bien calientes."
            ],
            "notes": [],
            "handwritten_notes": []
        }
    ],
    "continues_next": False,
    "legibility": "good",
    "rotation_issue": False
}

# Page 218
pages["page_218"] = {
    "page": "218",
    "file": "recetario _218.jpg",
    "model": "claude-3-7-sonnet",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "PASTA BASICA PARA CREPES DULCES",
            "normalized_title": "pasta basica para crepes dulces",
            "is_continuation": False,
            "ingredients": [
                "1 Taza de harina cernida",
                "1/4 Cdita. de sal",
                "1 Cda. de azúcar",
                "3 Huevos ligeramente batidos",
                "1 1/2 Taza de leche",
                "2 Cdas. de mantequilla derretida"
            ],
            "steps": [
                "Cernir juntos la harina, la sal y el azúcar en un tazón.",
                "Aparte mezclar los huevos ligeramente batidos con la leche y la mantequilla derretida.",
                "Incorporar los ingredientes líquidos a los secos batiendo vigorosamente para evitar grumos, hasta tener una mezcla tersa.",
                "Dejar reposar la masa en refrigeración durante 30 minutos.",
                "Enmantequillar ligeramente una sartén caliente a fuego medio. Verter un poco de mezcla girando la sartén para cubrir la superficie.",
                "Cocinar hasta que los bordes doren ligeramente, voltear unos segundos y retirar.",
                "Repetir hasta terminar la masa rindiendo de 18 a 20 crepes."
            ],
            "notes": [],
            "handwritten_notes": [
                "Anotación al calce: '18 a 20 crepes'."
            ]
        },
        {
            "kind": "recipe",
            "title": "CREPES FLAMBEE",
            "normalized_title": "crepes flambee",
            "is_continuation": False,
            "ingredients": [
                "18-20 Crepes preparadas",
                "Mantequilla",
                "Azúcar",
                "Jugo de naranja natural",
                "Jugo de limón",
                "Licor de naranja (Grand Marnier o Cointreau)",
                "Ron para flambear"
            ],
            "steps": [
                "En una sartén amplia a fuego suave, derretir mantequilla con azúcar, jugo de naranja y unas gotas de jugo de limón hasta formar un almíbar suave.",
                "Doblar las crepes en cuatro formando triángulos o pañuelos, colocándolas en la sartén para que absorban la salsa caliente.",
                "Rociar con licor de naranja y ron tibio. Con cuidado acercar una flama para flambear hasta que se evapore el alcohol.",
                "Servir inmediatamente bien calientes bañadas con la salsa."
            ],
            "notes": [
                "De origen polinesio."
            ],
            "handwritten_notes": []
        },
        {
            "kind": "recipe",
            "title": "CREPES ENSUEÑO DE LIMON",
            "normalized_title": "crepes ensueno de limon",
            "is_continuation": False,
            "ingredients": [
                "Crepes preparadas",
                "1 1/2 Taza de azúcar",
                "Jugo de limón natural",
                "Ralladura de limón",
                "Mantequilla"
            ],
            "steps": [
                "Calentar al fuego la mantequilla junto con 1 1/2 taza de azúcar, jugo de limón y ralladura hasta disolver el azúcar y formar un jarabe.",
                "Sumergir y bañar las crepes dobladas en el jarabe al fuego.",
                "Servir calientes con el almíbar de limón por encima."
            ],
            "notes": [],
            "handwritten_notes": [
                "Anotación al calce: '1 1/2 taza de azúcar, al fuego el limón'."
            ]
        }
    ],
    "continues_next": False,
    "legibility": "good",
    "rotation_issue": False
}

# Page 219
pages["page_219"] = {
    "page": "219",
    "file": "recetario _219.jpg",
    "model": "claude-3-7-sonnet",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "GALLETAS SUIZAS",
            "normalized_title": "galletas suizas",
            "is_continuation": False,
            "ingredients": [
                "1 Taza de mantequilla",
                "1/2 Taza de azúcar glass cernida",
                "1 Huevo",
                "2 Tazas de harina cernida",
                "1/2 Taza de nueces o almendras picadas",
                "Coco rallado o esencia al gusto (opcional)"
            ],
            "steps": [
                "Batir la mantequilla hasta acremar y agregar poco a poco el azúcar glass cernida.",
                "Añadir el huevo y batir hasta integrar bien.",
                "Incorporar la harina cernida mezclando hasta obtener una masa suave.",
                "Agregar las nueces o almendras picadas y esencia al gusto.",
                "Formar bolitas o rollos pequeños y rodarlos por nuez picada o coco rallado.",
                "Colocar en latas de hornear y hornear a 350°F por 12 a 15 minutos hasta que estén apenas doradas."
            ],
            "notes": [],
            "handwritten_notes": []
        },
        {
            "kind": "recipe",
            "title": "GALLETAS BASICAS",
            "normalized_title": "galletas basicas",
            "is_continuation": False,
            "ingredients": [
                "1 Taza de margarina o mantequilla",
                "1 Taza de azúcar",
                "2 Huevos",
                "1 Cdita. de vainilla",
                "3 Tazas de harina",
                "2 Cditas. de polvo de hornear",
                "1/2 Cdita. de sal"
            ],
            "steps": [
                "Cremar la margarina con el azúcar. Añadir los huevos uno a uno batiendo bien, y luego la vainilla.",
                "Cernir la harina con el polvo de hornear y la sal. Añadir a la crema integrando con espátula hasta formar una masa suave.",
                "Refrigerar la masa durante 1 hora para facilitar su manejo.",
                "Estirar sobre superficie enharinada a 1/2 cm de grosor y cortar figuras deseadas.",
                "Colocar en bandejas y hornear a 375°F por 8 a 10 minutos."
            ],
            "notes": [
                "Variaciones: Galletas morenas (sustituyendo parte de azúcar por azúcar morena y especias), árboles de navidad y festivas decoradas con glasé."
            ],
            "handwritten_notes": []
        }
    ],
    "continues_next": False,
    "legibility": "good",
    "rotation_issue": False
}

# Page 220
pages["page_220"] = {
    "page": "220",
    "file": "recetario _220.jpg",
    "model": "claude-3-7-sonnet",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "PASTEL NAVIDEÑO DE CIRUELA Y MANZANA",
            "normalized_title": "pastel navideno de ciruela y manzana",
            "is_continuation": False,
            "ingredients": [
                "2 Tazas de harina",
                "1 1/2 Taza de azúcar",
                "1 Cdita. de bicarbonato de sodio",
                "1 Cdita. de canela en polvo",
                "1/2 Cdita. de pimienta gorda molida (allspice)",
                "1/2 Cdita. de sal",
                "3 Huevos",
                "1 Taza de aceite",
                "1 Taza de puré de manzana",
                "1 Taza de ciruelas pasas picadas",
                "1 Taza de nueces picadas"
            ],
            "steps": [
                "Cernir juntos los ingredientes secos: harina, azúcar, bicarbonato de sodio, canela, pimienta gorda y sal.",
                "En otro tazón, batir los huevos ligeramente; añadir el aceite y el puré de manzana mezclando bien.",
                "Integrar los ingredientes secos a la mezcla líquida con movimientos suaves.",
                "Pasar las ciruelas pasas picadas y las nueces picadas por un poco de harina para que no se vayan al fondo, y añadirlas a la masa de manera envolvente.",
                "Verter la masa en un molde de corona o chimenea previamente engrasado y enharinado.",
                "Hornear a 350°F por 1 hora a 1 hora y 15 minutos, hasta que al insertar un palillo salga limpio.",
                "Dejar reposar 15 minutos antes de desmoldar sobre una rejilla."
            ],
            "notes": [
                "Encabezado: Beatrice's kitchen."
            ],
            "handwritten_notes": []
        }
    ],
    "continues_next": False,
    "legibility": "good",
    "rotation_issue": False
}

# Page 221
pages["page_221"] = {
    "page": "221",
    "file": "recetario _221.jpg",
    "model": "claude-3-7-sonnet",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "PAN DE LIMON NAVIDEÑO",
            "normalized_title": "pan de limon navideno",
            "is_continuation": False,
            "ingredients": [
                "2 Tazas de harina",
                "1/4 Cucharadita de sal",
                "1 Taza de azúcar",
                "1/3 Taza de leche",
                "2 Cucharaditas de rallo de limón",
                "1 1/2 Cucharaditas de polvo de hornear",
                "1/2 Taza de mantequilla o margarina (4 oz)",
                "2 Huevos",
                "1/2 Taza de nueces picadas",
                "JARABE: 1/2 Taza de jugo de limón",
                "JARABE: 1/3 Taza de azúcar"
            ],
            "steps": [
                "Batir la mantequilla con la taza de azúcar hasta que esté cremosa.",
                "Añadir los huevos uno a uno, batiendo bien tras cada adición.",
                "Cernir el harina, el polvo de hornear y la sal; agregarlos a la mantequilla alternando con la leche.",
                "Agregar las nueces picadas y el rallo de limón.",
                "Colocar la mezcla repartida en dos moldes de pan engrasados de 7x3 1/2x2 pulgadas.",
                "Colocar los moldes en una lata de galletas y hornear a 350° por 45 minutos.",
                "JARABE: Combinar el jugo de limón y el azúcar y cocinar revolviendo constantemente por un minuto.",
                "Echar este jarabe caliente sobre los panes inmediatamente después de sacarlos del horno.",
                "Dejarlos 10 minutos en los moldes para absorber el jarabe y luego dejar enfriar completamente sobre una parrilla."
            ],
            "notes": [
                "INSTITUTO FEMENINO DE ESTUDIOS SUPERIORES, HOGAR EMPRESA, ARTE CULINARIO (TECNICAS DULCES), CATEDRATICA: SRA. BEATRIZ DE ARZU."
            ],
            "handwritten_notes": [
                "Anotación '4 oz.' al lado de mantequilla.",
                "Corrección manuscrita 'de galletas' sustituyendo a 'entera'."
            ]
        }
    ],
    "continues_next": False,
    "legibility": "good",
    "rotation_issue": False
}

# Page 222
pages["page_222"] = {
    "page": "222",
    "file": "recetario _222.jpg",
    "model": "claude-3-7-sonnet",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "CARNE CON VINO",
            "normalized_title": "carne con vino",
            "is_continuation": False,
            "ingredients": [
                "2 Libras de lomito o rochoy en cubos",
                "1/4 Taza de mantequilla",
                "1/2 Libra de hongos en tajadas",
                "6 Tiras de tocino en cuadritos",
                "2 Cucharadas de harina",
                "1 Cucharadita de azúcar",
                "Sal al gusto",
                "Tomillo al gusto",
                "1 Hoja de laurel",
                "1 Taza de vino tinto seco",
                "1 Taza de caldo de consomé de res",
                "Cebolla picada al gusto"
            ],
            "steps": [
                "Sofreír los hongos con la mantequilla y la cebolla picada; apartar.",
                "Freír el tocino muy bien hasta que esté crujiente; apartar.",
                "En la grasa del tocino, dorar la carne hecha en cubos previamente sazonada con sal.",
                "Añadir la harina, el azúcar, tomillo, sal y la hoja de laurel.",
                "Añadir el caldo de consomé y el vino tinto seco.",
                "Verificar sazón. Cocer tapado, revolviendo lentamente hasta lograr su completa cocción.",
                "Si el líquido se hubiera evaporado, agregar más caldo o vino.",
                "Servir sobre arroz blanco caliente."
            ],
            "notes": [
                "instituto femenino de estudios superiores, departamento de hogar empresa, arte culinario, hogar empresa II, catedrática: AEH. Margarita de Sánchez."
            ],
            "handwritten_notes": []
        }
    ],
    "continues_next": False,
    "legibility": "good",
    "rotation_issue": False
}

# Page 223
pages["page_223"] = {
    "page": "223",
    "file": "recetario _223.jpg",
    "model": "claude-3-7-sonnet",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "MOLDE DE PAPAS HORNEADAS",
            "normalized_title": "molde de papas horneadas",
            "is_continuation": False,
            "ingredients": [
                "2 Libras de papas cortadas en lascas finas",
                "2 Cucharadas de mantequilla",
                "1 Diente de ajo machacado",
                "1 Cucharadita de sal",
                "1 Cucharadita de pimienta",
                "1 Taza de queso cheddar rallado",
                "1 1/4 Taza de leche",
                "2/3 Taza de crema",
                "1 Huevo grande batido",
                "Perejil picado para decorar"
            ],
            "steps": [
                "En un molde para hornear engrasado, hacer capas alternadas de papas cortadas en lascas finas con el queso cheddar rallado.",
                "En un tazón aparte, unir la crema con la leche, la sal, pimienta, ajo machacado, mantequilla y el huevo batido.",
                "Vertir la mezcla líquida sobre las capas de papas en el molde.",
                "Hornear a 375 grados por 1 hora hasta que las papas estén tiernas y la superficie dorada.",
                "Sacar y servir caliente, espolvoreando con perejil picado para decorar."
            ],
            "notes": [
                "instituto femenino de estudios superiores, departamento de hogar empresa, arte culinario, hogar empresa II, catedrática: AEH. Margarita de Sánchez."
            ],
            "handwritten_notes": []
        }
    ],
    "continues_next": False,
    "legibility": "good",
    "rotation_issue": False
}

# Page 224
pages["page_224"] = {
    "page": "224",
    "file": "recetario _224.jpg",
    "model": "claude-3-7-sonnet",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "ENSALADA ROMANOFF",
            "normalized_title": "ensalada romanoff",
            "is_continuation": False,
            "ingredients": [
                "SALSA MIL ISLAS: 1 Taza de crema",
                "SALSA MIL ISLAS: 1 Taza de mayonesa",
                "SALSA MIL ISLAS: 6 Cucharadas de ketchup",
                "SALSA MIL ISLAS: 1 Cucharada de mostaza",
                "SALSA MIL ISLAS: 2 Pepinillos picaditos finos",
                "SALSA MIL ISLAS: 1 Cucharada de cognac",
                "SALSA MIL ISLAS: Tabasco al gusto",
                "SALSA MIL ISLAS: Sal y pimienta al gusto",
                "ENSALADA: 1 Taza de arvejas cocidas",
                "ENSALADA: 1-2 Pechugas de pollo cocidas y desmenuzadas",
                "ENSALADA: 4 Onzas de jamón en cuadritos",
                "ENSALADA: 1 Taza de queso cheddar ó monterrey jack rallado",
                "ENSALADA: 4 Tazas de lechuga bien lavada y picada (preparada)",
                "ENSALADA: 4 Huevos duros en mitades",
                "ENSALADA: 1/2 Taza de tocino picadito y frito",
                "ENSALADA: 4 Tajadas de pan tostado con mantequilla",
                "ENSALADA: 2 Tomates en tajadas (pelados)"
            ],
            "steps": [
                "Para la salsa mil islas: mezclar en un tazón la crema, mayonesa, ketchup, mostaza, pepinillos picados finos, cognac, unas gotas de tabasco, sal y pimienta al gusto.",
                "Cortar las tajadas de pan tostado en cubitos.",
                "Armar la ensalada en un bowl de vidrio transparente por capas: empezar por el pan tostado con mantequilla, seguido de lechuga picada, el pollo desmenuzado, los huevos duros, el queso cheddar o monterrey jack, un baño de salsa rosada, otra capa de lechuga, jamón en cuadritos, tocino frito crujiente y arvejas cocidas.",
                "Decorar con las tajadas de tomate peladas.",
                "Servir el resto de la salsa rosada al lado."
            ],
            "notes": [
                "instituto femenino de estudios superiores, departamento de hogar empresa, segundo trimestre, hogar empresa II, catedrática: AEH. Margarita de Sánchez."
            ],
            "handwritten_notes": []
        }
    ],
    "continues_next": False,
    "legibility": "good",
    "rotation_issue": False
}

# Page 226
pages["page_226"] = {
    "page": "226",
    "file": "recetario _226.jpg",
    "model": "claude-3-7-sonnet",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "BOLITAS DE COCO",
            "normalized_title": "bolitas de coco",
            "is_continuation": False,
            "ingredients": [
                "1 Paquete de galletas maría molidas",
                "1 Lata de leche condensada",
                "1 1/2 Taza de coco rallado",
                "Coco rallado adicional para cubrir"
            ],
            "steps": [
                "Unir los tres primeros ingredientes (galletas maría molidas, leche condensada y 1 1/2 taza de coco rallado) hasta formar una pasta compacta.",
                "Dar forma de bolitas con las manos.",
                "Pasar cada bolita por coco rallado adicional hasta cubrirlas por completo.",
                "Enfriar en la refrigeradora antes de servir."
            ],
            "notes": [
                "instituto femenino de estudios superiores, departamento de hogar empresa, arte culinario, hogar empresa II, catedrática: AEH. Margarita de Sánchez."
            ],
            "handwritten_notes": []
        },
        {
            "kind": "recipe",
            "title": "MERENGUES DE NARANJA Y COCO",
            "normalized_title": "merengues de naranja y coco",
            "is_continuation": False,
            "ingredients": [
                "1 Paquete de galletas maría molidas",
                "4-6 Onzas de mantequilla derretida (se puede usar más)",
                "1 Huevo",
                "Canela en polvo al gusto",
                "1 Bote de jalea de naranja",
                "Turrón cocido",
                "Coco rallado"
            ],
            "steps": [
                "En el procesador, mezclar las galletas maría molidas, mantequilla derretida, huevo y canela en polvo para formar la costra.",
                "Colocar y presionar la costra de galleta en una lata de hornear sin engrasar.",
                "Encima de la costra vertirle uniformemente el bote de jalea de naranja.",
                "Cubrir con turrón cocido mezclado con coco rallado.",
                "Poner a hornear a 300 grados por 20-25 minutos, hasta que seque el turrón.",
                "Dejar enfriar y cortar en cuadritos."
            ],
            "notes": [
                "instituto femenino de estudios superiores, departamento de hogar empresa, arte culinario, hogar empresa II, catedrática: AEH. Margarita de Sánchez."
            ],
            "handwritten_notes": []
        }
    ],
    "continues_next": False,
    "legibility": "good",
    "rotation_issue": False
}

# Page 226-1
pages["page_226_1"] = {
    "page": "226-1",
    "file": "recetario _226_1.jpg",
    "model": "claude-3-7-sonnet",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "PECHUGAS CORDON BLEU",
            "normalized_title": "pechugas cordon bleu",
            "is_continuation": False,
            "ingredients": [
                "2 Paquetes de pechugas deshuesadas (8 unidades)",
                "1/2 Libra de jamón virginia (u otro)",
                "1/2 Libra de queso suizo rodajeado",
                "Harina sazonada (con sal, pimienta y paprika)",
                "Huevo batido",
                "Miga de pan o corn-flakes molido con queso parmesano",
                "Aceite bien caliente (para freír)",
                "SALSA: 1 Sobre de crema de hongos",
                "SALSA: 3 Tazas de leche",
                "SALSA: 1/2 Taza de crema",
                "SALSA: Hongos tajeados fritos en mantequilla"
            ],
            "steps": [
                "Cocer las pechugas (no muy cocidas) en caldo con consomé. Sacar y hacer un corte de bolsillo por el medio.",
                "Ir rellenando cada una de las pechugas con jamón y queso; prensar con palillo de madera.",
                "Pasar por el empanizado empezando por la harina sazonada con sal, pimienta y paprika, luego por el huevo batido y por último por la miga de pan o corn-flakes mezclada con queso parmesano.",
                "Freír en suficiente aceite caliente (no en grasa profunda) hasta dorar bien por ambos lados.",
                "Aparte hacer la salsa disolviendo la crema de hongos en 3 tazas de leche, calentar hasta espesar, incorporar la 1/2 taza de crema y los hongos tajeados previamente fritos en mantequilla.",
                "Servir las pechugas bañadas con la salsa de hongos."
            ],
            "notes": [
                "instituto femenino de estudios superiores, departamento de hogar empresa, arte culinario, hogar empresa II, catedrática: AEH. Margarita de Sánchez."
            ],
            "handwritten_notes": [
                "Anotaciones manuscritas: 'pan' sobre corn-flakes, 'queso parmesano' añadido a la miga, sal, pimienta y paprika en harina, '3' tazas de leche corrigiendo a 1, y 'hongos tajeados fritos en mantequilla'."
            ]
        }
    ],
    "continues_next": False,
    "legibility": "good",
    "rotation_issue": False
}

# Page 227
pages["page_227"] = {
    "page": "227",
    "file": "recetario _227.jpg",
    "model": "claude-3-7-sonnet",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "ROAST BEEF",
            "normalized_title": "roast beef",
            "is_continuation": False,
            "ingredients": [
                "1 Lomito limpio entero",
                "3-4 Cucharadas de mostaza",
                "Sal y pimienta al gusto",
                "Aceite bien caliente",
                "1 Cebolla picada fina",
                "3 Ajos picados finos",
                "4 Tomates rodajeados",
                "Perejil colocho para decorar"
            ],
            "steps": [
                "Sobarse el lomito con sal y pimienta. Luego untar con la mostaza (preferiblemente un día antes).",
                "Aparte, freír en el aceite la cebolla picada y los ajos.",
                "En esa misma sartén colocar el lomito para sellarlo por todos sus lados.",
                "Sacar el lomito, disponerlo en una bandeja para horno y cubrirlo con las rodajas de tomate.",
                "Hornear a 350° por aproximadamente 30 minutos (debe quedar rosado al centro).",
                "Sacar del horno, dejar reposar, cortar en rodajas y servir decorado con perejil colocho."
            ],
            "notes": [
                "instituto femenino de estudios superiores, departamento de hogar empresa, segundo trimestre, hogar empresa II, catedrática: AEH. Margarita de Sánchez."
            ],
            "handwritten_notes": [
                "Horno 350°.",
                "'Preferible hecharle mostaza, sal y pimienta un día antes para que tenga más sabor.'"
            ]
        }
    ],
    "continues_next": False,
    "legibility": "good",
    "rotation_issue": False
}

# Page 228
pages["page_228"] = {
    "page": "228",
    "file": "recetario _228.jpg",
    "model": "claude-3-7-sonnet",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "VERDURAS GLASEADAS",
            "normalized_title": "verduras glaseadas",
            "is_continuation": False,
            "ingredients": [
                "Guicoyitos y zanahorias",
                "1 Cucharadita de sal",
                "1/4 Taza de caldo de pollo",
                "1 Cucharada de azúcar fina",
                "2 Cucharadas de mantequilla",
                "2 Cucharadas de perejil picado fino"
            ],
            "steps": [
                "Cocer los guicoyitos y zanahorias de 5 a 8 minutos en agua con la sal, deseando que queden ligeramente duras (al dente); escurrir.",
                "Aparte combinar en una sartén el caldo de pollo, azúcar fina y mantequilla; calentar y dejar hervir suavemente hasta reducir a la mitad formando un almíbar ligero.",
                "Agregar las verduras escurridas y el perejil picado fino, salteando para cubrirlas con el glaseado.",
                "Servir caliente."
            ],
            "notes": [
                "instituto femenino de estudios superiores, departamento de hogar empresa, hogar empresa II, arte culinario, catedrática: AEH. Margarita de Sánchez."
            ],
            "handwritten_notes": []
        }
    ],
    "continues_next": False,
    "legibility": "good",
    "rotation_issue": False
}

# Page 229
pages["page_229"] = {
    "page": "229",
    "file": "recetario _229.jpg",
    "model": "claude-3-7-sonnet",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "POTPURRI DE VEGETALES",
            "normalized_title": "potpurri de vegetales",
            "is_continuation": False,
            "ingredients": [
                "1 Taza de arvejas peladas",
                "1 Taza de ejotes cortados en trozos",
                "1 Coliflor grande separada en florecitas",
                "3/4 Taza de agua",
                "1 Lata de chiles pimientos",
                "2 Cucharadas de mantequilla o margarina",
                "1/2 Cucharadita de albahaca seca",
                "1/2 Cucharadita de sal",
                "1/2 Cucharadita de pimienta"
            ],
            "steps": [
                "Cocine los vegetales (arvejas, ejotes y coliflor) con los 3/4 taza de agua hirviendo o al vapor hasta que estén tiernos.",
                "Escurra el exceso de agua.",
                "Añada los chiles pimientos en tiras, la mantequilla o margarina, la albahaca seca, sal y pimienta.",
                "Saltee suavemente para mezclar los sabores antes de servir."
            ],
            "notes": [
                "Encabezado: Beatrice's kitchen."
            ],
            "handwritten_notes": []
        },
        {
            "kind": "recipe",
            "title": "ZANAHORIAS GLASEADAS",
            "normalized_title": "zanahorias glaseadas",
            "is_continuation": False,
            "ingredients": [
                "1 1/4 Libras de zanahorias baby",
                "1/3 Taza de azúcar morena",
                "2 Cucharadas de mantequilla o margarina",
                "1/2 Cucharadita de sal",
                "1/2 Cucharadita de rallo de naranja"
            ],
            "steps": [
                "Cocine las zanahorias baby en poca agua hirviendo sin sal o al vapor hasta que estén tiernas; escurra.",
                "Ponga el azúcar morena con la margarina, sal y el rallo de naranja en una olla amplia o sartén.",
                "Caliente a fuego medio hasta que empiece a formar burbujas.",
                "Añada las zanahorias baby y cocine a fuego suave, revolviendo ocasionalmente, hasta que estén bien glaseadas y calientes (aproximadamente 5 minutos).",
                "Servir caliente."
            ],
            "notes": [
                "Encabezado: Beatrice's kitchen."
            ],
            "handwritten_notes": []
        }
    ],
    "continues_next": False,
    "legibility": "good",
    "rotation_issue": False
}

# Page 230
pages["page_230"] = {
    "page": "230",
    "file": "recetario _230.jpg",
    "model": "claude-3-7-sonnet",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "BOLITAS DE COCO",
            "normalized_title": "bolitas de coco",
            "is_continuation": False,
            "ingredients": [
                "1 Paquete de galletas maría molidas",
                "1 Lata de leche condensada",
                "1 1/2 Taza de coco rallado",
                "Coco rallado adicional para cubrir"
            ],
            "steps": [
                "Unir los tres primeros ingredientes (galletas maría molidas, leche condensada y 1 1/2 taza de coco rallado) hasta formar una masa homogénea.",
                "Formar bolitas del tamaño deseado.",
                "Pasar y rodar las bolitas por más coco rallado.",
                "Enfriar y servir."
            ],
            "notes": [
                "instituto femenino de estudios superiores, departamento de hogar empresa, arte culinario, hogar empresa II, catedrática: AEH. Margarita de Sánchez."
            ],
            "handwritten_notes": []
        },
        {
            "kind": "recipe",
            "title": "MERENGUES DE NARANJA Y COCO",
            "normalized_title": "merengues de naranja y coco",
            "is_continuation": False,
            "ingredients": [
                "1 Paquete de galletas maría molidas",
                "4-6 Onzas de mantequilla derretida (se puede usar más)",
                "1 Huevo",
                "Canela en polvo al gusto",
                "1 Bote de jalea de naranja",
                "Turrón cocido",
                "Coco rallado"
            ],
            "steps": [
                "Preparar la base procesando las galletas maría con la mantequilla derretida, el huevo y canela en polvo.",
                "Colocar la mezcla en una lata para hornear sin engrasar y presionar firmemente formando una costra pareja.",
                "Vertir encima la jalea de naranja cubriendo la costra.",
                "Colocar turrón cocido mezclado con coco rallado encima de la jalea.",
                "Hornear a 300 grados por 20 a 25 minutos, hasta que seque el turrón.",
                "Dejar enfriar y cortar en cuadritos."
            ],
            "notes": [
                "instituto femenino de estudios superiores, departamento de hogar empresa, arte culinario, hogar empresa II, catedrática: AEH. Margarita de Sánchez."
            ],
            "handwritten_notes": []
        }
    ],
    "continues_next": False,
    "legibility": "good",
    "rotation_issue": False
}

# Page 231
pages["page_231"] = {
    "page": "231",
    "file": "recetario _231.jpg",
    "model": "claude-3-7-sonnet",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "PAPAS RELLENAS",
            "normalized_title": "papas rellenas",
            "is_continuation": False,
            "ingredients": [
                "8 Papas grandes con su cáscara",
                "4 Cucharadas de mantequilla",
                "2 Cucharaditas de sal",
                "1 Cucharadita de pimienta negra",
                "1 Cucharadita de nuez moscada",
                "4 Huevos separados",
                "2 Cucharadas de crema",
                "2 Cucharadas de leche",
                "Queso parmesano para gratinar",
                "Perejil picado para decorar"
            ],
            "steps": [
                "Limpiar muy bien las papas enteras con su cáscara.",
                "Poner en una lata y hornear a 425 grados por una hora hasta que estén cocidas y suaves al tacto.",
                "Partir por la mitad a lo largo y sacar la pulpa con cuidado con una cuchara, dejando las cáscaras intactas.",
                "Hacer puré con la papa extraída, mantequilla, sal, pimienta negra, nuez moscada, yemas de huevo, crema y leche.",
                "Batir las claras de huevo a punto de nieve y agregarlas de último con movimientos suaves y envolventes.",
                "Meter las costras de papa solas al horno a 425°F por 10 a 15 minutos para que se sequen y se tornen crujientes.",
                "Rellenar cada una de las cáscaras tostadas con el puré esponjoso.",
                "Espolvorear con queso parmesano y hornear 10 a 15 minutos hasta que doren y gratinen.",
                "Decorar con perejil picado al servir."
            ],
            "notes": [
                "instituto femenino de estudios superiores, departamento de hogar empresa, hogar empresa II, arte culinario, catedrática: AEH. Margarita de Sánchez."
            ],
            "handwritten_notes": []
        }
    ],
    "continues_next": False,
    "legibility": "good",
    "rotation_issue": False
}

# Page 232
pages["page_232"] = {
    "page": "232",
    "file": "recetario _232.jpg",
    "model": "claude-3-7-sonnet",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "TIRAMISU",
            "normalized_title": "tiramisu",
            "is_continuation": False,
            "ingredients": [
                "2 Paquetes de queso mascarpone",
                "3/4 Taza de crema",
                "3/4 Taza de azúcar",
                "5 Cucharadas de café instantáneo disuelto espeso",
                "1/2 a 3/4 Taza de licor de café",
                "Galletas chiquiadores",
                "Cocoa amarga en polvo"
            ],
            "steps": [
                "Unir el café espeso con el licor de café (1/2 a 3/4 taza).",
                "Remojar ligeramente los chiquiadores en la mezcla de café y licor e irlos colocando en el fondo de un molde pyrex.",
                "Aparte batir muy bien el queso mascarpone con la crema y el azúcar hasta obtener una consistencia suave y cremosa.",
                "Colocar una capa de crema sobre los chiquiadores y espolvorear cocoa amarga encima.",
                "Continuar alternando capas de chiquiadores remojados, crema de queso y cocoa, hasta formar 3 capas completas.",
                "Refrigerar de 3 a 4 horas antes de servir."
            ],
            "notes": [
                "instituto femenino de estudios superiores, departamento de hogar empresa, hogar empresa II, arte culinario, catedrática: AEH. Margarita de Sánchez."
            ],
            "handwritten_notes": [
                "Queso mascarpone 'en multimart o pharma'.",
                "Crema corregida a '3/4 taza' (tachado 1 1/2).",
                "Café instantáneo corregido a '5 cucharadas espesas'."
            ]
        }
    ],
    "continues_next": False,
    "legibility": "good",
    "rotation_issue": False
}

# Page 233
pages["page_233"] = {
    "page": "233",
    "file": "recetario _233.jpg",
    "model": "claude-3-7-sonnet",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "ARROZ ESPECIAL",
            "normalized_title": "arroz especial",
            "is_continuation": False,
            "ingredients": [
                "1 Libra de arroz cocinado con mantequilla y consomé",
                "3 Tazas de salsa blanca (4 tazas de leche, 3 cdas. harina, cebolla, 2 onzas de mantequilla, crema)",
                "1 Frasco pequeño de palmito cortado en cuadritos",
                "10 Onzas de queso monterrey jack rallado",
                "Queso parmesano rallado al gusto"
            ],
            "steps": [
                "Engrasar un pyrex rectangular.",
                "Colocar en el fondo una capa de arroz cocido con mantequilla y consomé.",
                "Añadir una capa de salsa blanca, trocitos de palmito y queso monterrey jack (rallado o en rodajas).",
                "Continuar alternando capas hasta terminar con arroz.",
                "Espolvorear generosamente con queso parmesano rallado (y otro queso rallado si hubiera).",
                "Tapar con papel de aluminio y hornear a 350 grados por 20 minutos."
            ],
            "notes": [
                "instituto femenino de estudios superiores, departamento de hogar empresa, arte culinario, hogar empresa II, catedrática: AEH. Margarita de Sánchez."
            ],
            "handwritten_notes": [
                "'pyrex rectangular engrasado' anotado al lado del título.",
                "'con papel de aluminio' anotado al pie para el horneado."
            ]
        }
    ],
    "continues_next": False,
    "legibility": "good",
    "rotation_issue": False
}

# Page 234
pages["page_234"] = {
    "page": "234",
    "file": "recetario _234.jpg",
    "model": "claude-3-7-sonnet",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "PASTEL DE JENGIBRE",
            "normalized_title": "pastel de jengibre",
            "is_continuation": False,
            "ingredients": [
                "1/2 Taza de mantequilla",
                "1/2 Taza de azúcar",
                "1 Huevo",
                "2 1/2 Tazas de harina",
                "1 1/2 Cucharadita de bicarbonato",
                "1 Cucharadita de royal (polvo de hornear)",
                "1 Cucharadita de canela en polvo",
                "1 1/2 Cucharadita de jengibre en polvo",
                "1/2 Cucharadita de sal",
                "1/2 Taza de miel karo",
                "1/2 Taza de miel de abeja",
                "1 Taza de agua caliente"
            ],
            "steps": [
                "Derretir la mantequilla, agregar el huevo y el azúcar bien batidos.",
                "Cernir juntos los ingredientes sólidos: harina, bicarbonato, royal, canela, jengibre y sal.",
                "En otro tazón mezclar los líquidos restantes: miel karo, miel de abeja y el agua caliente.",
                "Agregar a la mezcla de mantequilla y huevos los sólidos y líquidos de manera alternada.",
                "Verter en molde engrasado y hornear a 350 grados por 30 minutos aproximadamente."
            ],
            "notes": [
                "RECETAS EXTRA."
            ],
            "handwritten_notes": []
        },
        {
            "kind": "recipe",
            "title": "BOLAS DE CAMOTE",
            "normalized_title": "bolas de camote",
            "is_continuation": False,
            "ingredients": [
                "2 1/2 Tazas de puré de camote caliente",
                "3 Onzas de mantequilla",
                "1/2 Taza de azúcar",
                "1/2 Cucharadita de sal",
                "1 Cucharadita de vainilla",
                "10 Angelitos blancos grandes (malvaviscos)",
                "1/3 Taza de miel de abejas",
                "2 Onzas de mantequilla",
                "1 Taza de nueces picadas"
            ],
            "steps": [
                "Unir el puré de camote caliente con las 3 onzas de mantequilla, el azúcar, sal y vainilla hasta integrar bien.",
                "Hacer bolas con la masa y colocarles un angelito blanco grande en medio, envolviéndolo por completo.",
                "Aparte derretir las 2 onzas de mantequilla con el 1/3 taza de miel de abejas.",
                "Pasar cada bola de camote por la mezcla de miel y mantequilla y rodarla en las nueces picadas para cubrirlas.",
                "Poner en una bandeja de hornear a 300 grados por 20 a 25 minutos."
            ],
            "notes": [
                "RECETAS EXTRA."
            ],
            "handwritten_notes": []
        }
    ],
    "continues_next": False,
    "legibility": "good",
    "rotation_issue": False
}

# Page 235
pages["page_235"] = {
    "page": "235",
    "file": "recetario _235.jpg",
    "model": "claude-3-7-sonnet",
    "skip_reason": "",
    "items": [
        {
            "kind": "tip",
            "title": "PROGRAMA: ARTE CULINARIO I",
            "normalized_title": "programa arte culinario i",
            "is_continuation": False,
            "ingredients": [],
            "steps": [],
            "notes": [
                "instituto femenino de estudios superiores, departamento de hogar empresa, hogar empresa II, primer trimestre, arte culinario I, catedrática: AEH. Margarita de Sánchez.",
                "OBJETIVO: Complementar de una forma más variada y elaborada en las recetas, a las clases de Técnicas Culinarias Saladas y Dulces. Así como ir elaborando menús.",
                "Técnica de Pastas: Fussilli con salsa de chile pimiento, Lasagna de pollo especial.",
                "Técnica de Crepas: Crepas de pollo en salsa de hongos, Crepas dulces de fresa.",
                "Técnica de Pasteles Esponjosos: Brazo Gitano, Pastel Esponjoso de Frutas.",
                "Técnica de Pies: Pie de Puerro, Quiche Lorraine, Pie de Higo Especial.",
                "Menú 1 Cuaresma: Camarones Florentinos, Pastel de Banano.",
                "Menú 2 Cuaresma: Pescado con chile pimiento, Atún en Cacerola, Pastel de Zanahoria.",
                "Menú 3 Cuaresma: Pescado empanizado con salsa Tártara, Pastel de helado de café.",
                "Bar de Ensaladas.",
                "Menú Especial: Pollo en salsa de Albaricoques, Ensalada de espinaca y mandarinas, Brownies decorados con chocolate y helado."
            ],
            "handwritten_notes": []
        }
    ],
    "continues_next": False,
    "legibility": "good",
    "rotation_issue": False
}

# Write out all page files
for key, data in pages.items():
    file_path = PAGES_DIR / f"{key}.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"Wrote {file_path}")

print(f"Successfully wrote {len(pages)} page files.")
