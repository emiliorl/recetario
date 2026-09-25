import json
from pathlib import Path

PAGES_DIR = Path("cache/pages")
PAGES_DIR.mkdir(parents=True, exist_ok=True)

pages = {}

# Page 236
pages["page_236"] = {
    "page": "236",
    "file": "recetario _236.jpg",
    "model": "gemini-3.8-flash",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "PESCADO CON CHILE PIMIENTO",
            "normalized_title": "pescado con chile pimiento",
            "is_continuation": False,
            "ingredients": [
                "10 Filetes de pescado (curvina) salpimientados",
                "1 Taza de crema",
                "2 Cebollas grandes en gajitos",
                "1 Lata de chile pimiento morrón grande picado",
                "Queso parmesano",
                "Pimienta blanca (manuscrito)",
                "Mantequilla (para freír cebollas)"
            ],
            "steps": [
                "Se salpimientan los filetes de pescado con sal y pimienta blanca, luego freír las cebollas cortadas en gajitos en mantequilla.",
                "Colocar en un pyrex los filetes, luego las cebollas y hornear por 5 minutos.",
                "Por último, licuar la crema con los chiles morrones para hacer la salsa, agregarla sobre el pescado y hornear nuevamente a 350 grados por 15 a 20 minutos.",
                "Espolvorear con queso parmesano y gratinar."
            ],
            "notes": "Instituto Femenino de Estudios Superiores (IFES) - Catedrática AEH Margarita de Sánchez. Anotación manuscrita al pie: Se cocina el pescado con la cebolla, se coloca en un pyrex y se hornea por 5 minutos. Luego se agrega la salsa y se hornea nuevamente por 15 a 20 min."
        }
    ]
}

# Page 237
pages["page_237"] = {
    "page": "237",
    "file": "recetario _237.jpg",
    "model": "gemini-3.8-flash",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "CREPAS DULCES DE FRESA",
            "normalized_title": "crepas dulces de fresa",
            "is_continuation": False,
            "ingredients": [
                "1 Receta de crepas dulces",
                "1 Queso crema batido de 8 onzas (Pharma o Philadelphia)",
                "1 Lata de leche condensada",
                "1 Caja de fresas en cuadritos",
                "Jugo de 1 limón",
                "Ralladura de 1 limón",
                "Crema Chantilly",
                "2 Tazas de fresas licuadas (para la salsa)",
                "2 Tazas de azúcar (para la salsa)",
                "Colorante vegetal (opcional, para la salsa)"
            ],
            "steps": [
                "Se tienen preparadas las crepas dulces (si se desea se pueden hacer desde un día antes).",
                "Para el relleno, mezclar el queso crema batido con la leche condensada, el jugo y la ralladura de limón, y las fresas picadas en cuadritos.",
                "Rellenar las crepas con la mezcla de queso y fresas, y colocarlas en un pyrex.",
                "Para la salsa: licuar 2 tazas de fresas con 2 tazas de azúcar y colorante vegetal opcional, y poner a hervir para que espese.",
                "Bañar las crepas con la salsa caliente de fresas y decorar con crema Chantilly."
            ],
            "notes": "Edith's Kitchen."
        }
    ]
}

# Page 238
pages["page_238"] = {
    "page": "238",
    "file": "recetario _238.jpg",
    "model": "gemini-3.8-flash",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "SALSA DE LIMÓN",
            "normalized_title": "salsa de limon",
            "is_continuation": False,
            "ingredients": [
                "1 Taza de azúcar",
                "2 Cucharadas de maicena",
                "1 Taza de agua",
                "1/4 Taza de mantequilla o margarina",
                "2 Cucharaditas de rallo de limón",
                "1 Pizca de sal",
                "1/4 Taza de jugo de limón"
            ],
            "steps": [
                "Combinar en una olla el azúcar y la maicena. Añadir 1 taza de agua y mezclar bien.",
                "Llevar a ebullición, revolviendo constantemente.",
                "Reducir el calor y dejar a fuego lento hasta que la mezcla esté transparente y espese (aproximadamente 5 minutos).",
                "Retirar del fuego, agregar la mantequilla o margarina, el rallo de limón, la sal y el jugo de limón.",
                "Servir tibio. Rinde para 2/3 de taza (15 a 18 porciones)."
            ],
            "notes": ""
        }
    ]
}

# Page 239
pages["page_239"] = {
    "page": "239",
    "file": "recetario _239.jpg",
    "model": "gemini-3.8-flash",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "SALSA DE MORAS",
            "normalized_title": "salsa de moras",
            "is_continuation": False,
            "ingredients": [
                "1 Cucharadita de rallo de limón",
                "3 Tazas de moras",
                "1 Cucharada de jugo de limón",
                "3/4 Cucharadita de canela en polvo",
                "1 1/2 Tazas de azúcar",
                "1 Cucharadita de mantequilla o margarina"
            ],
            "steps": [
                "Mezclar los ingredientes en el orden escrito dentro de una cacerola.",
                "Cocinar a fuego moderado hasta formar una salsa suave y brillante. Salen 2 tazas."
            ],
            "notes": ""
        }
    ]
}

# Page 240
pages["page_240"] = {
    "page": "240",
    "file": "recetario _240.jpg",
    "model": "gemini-3.8-flash",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "SALSA DE CARAMELO",
            "normalized_title": "salsa de caramelo",
            "is_continuation": False,
            "ingredients": [
                "1 1/2 Taza de azúcar",
                "2 Tazas de leche",
                "12 Yemas batidas",
                "1 Raja de canela"
            ],
            "steps": [
                "Hacer un caramelo claro con el azúcar en una olla.",
                "Agregarle con sumo cuidado la leche, las yemas batidas y la raja de canela.",
                "Hervir a fuego muy bajo hasta que se disuelva por completo el azúcar.",
                "Tener cuidado al mezclar debido a que la alta temperatura del caramelo puede cortar las yemas."
            ],
            "notes": ""
        }
    ]
}

# Page 241
pages["page_241"] = {
    "page": "241",
    "file": "recetario _241.jpg",
    "model": "gemini-3.8-flash",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "SALSA CALIENTE DE CHOCOLATE",
            "normalized_title": "salsa caliente de chocolate",
            "is_continuation": False,
            "ingredients": [
                "1 Taza de chocolate semi dulce (cobertura o chocolate chips)",
                "1/2 Taza de miel karo blanca",
                "1/4 Taza de crema pura",
                "1 Cucharada de mantequilla",
                "1 Cucharadita de vainilla"
            ],
            "steps": [
                "En un tazón de vidrio para microondas o baño María, mezclar el chocolate y la miel karo.",
                "Calentar a Medium Low de 4 a 4 1/2 minutos.",
                "Agregar poco a poco la crema pura y por último la mantequilla y la vainilla.",
                "Bañar el helado con esta salsa."
            ],
            "notes": "Marca de agua: Salsas Dulces. Nota al pie: Colocar la mezcla en una lata forrada con papel parafinado sin engrasar con una cucharadita (bastante separadas). Adornar con guindas. Hornear a 325° por aproximadamente 20 minutos hasta que estén ligeramente doradas. Para 15 a 20 porciones."
        }
    ]
}

# Page 242
pages["page_242"] = {
    "page": "242",
    "file": "recetario _242.jpg",
    "model": "gemini-3.8-flash",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "TIRAMISÚ DE FRESA",
            "normalized_title": "tiramisu de fresa",
            "is_continuation": False,
            "ingredients": [
                "2 Vasos de fresas machacadas",
                "4 Cucharadas de ron oscuro",
                "16 Chiqueadores",
                "3/4 Taza de café expreso",
                "1 Taza de queso crema suavizado",
                "1/3 Taza de azúcar",
                "2 Onzas de chocolate semi dulce rayado",
                "1 Taza de crema espesa"
            ],
            "steps": [
                "En un pequeño bol combina fresas y 1 cucharada de ron oscuro y déjelas marinar durante 30 minutos.",
                "Mientras tanto, coloca cuatro chiqueadores en cada una de las cuatro dulceras individuales.",
                "En una taza combina el café expreso y agrégale tres cucharadas de ron. Vierte esta mezcla de café y ron sobre los chiqueadores.",
                "En un bol mediano mezcla el queso crema, la crema espesa, el azúcar y bate bien.",
                "Coloca esta mezcla sobre los chiqueadores, y sobre ella las fresas marinadas.",
                "Espolvorea con chocolate semidulce rayado."
            ],
            "notes": ""
        }
    ]
}

# Page 243
pages["page_243"] = {
    "page": "243",
    "file": "recetario _243.jpg",
    "model": "gemini-3.8-flash",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "CREPAS RELLENAS DE MANZANA",
            "normalized_title": "crepas rellenas de manzana",
            "is_continuation": False,
            "ingredients": [
                "3 Huevos",
                "1 1/2 Taza de leche",
                "1 1/4 Taza de harina",
                "1/2 Cucharadita de royal",
                "2 Cucharadas de azúcar",
                "1/8 Cucharadita de sal",
                "2 Cucharadas de jugo de limón",
                "1 Cucharada de ron o cognac",
                "Margarina derretida",
                "1/3 Taza de margarina (para el relleno)",
                "3 Libras de manzanas peladas partidas en cuadritos (para el relleno)",
                "1/2 Taza de azúcar (para el relleno)",
                "1 Cucharadita de canela en polvo (para el relleno)",
                "1/4 Taza de azúcar (para espolvorear)",
                "1 Cucharadita de canela en polvo (para espolvorear)"
            ],
            "steps": [
                "Bata los huevos, agregue la leche, luego la harina, royal, azúcar y sal; mezcle bien. Añada margarina derretida, jugo de limón y ron o cognac.",
                "Caliente un sartén mediano, úntelo ligeramente de margarina, vierta un poco de masa solo a cubrir el fondo, deje orillas finas, dele vuelta al panqueque para que dore el otro lado.",
                "Saque la crepa, coloque porción de relleno en medio, enrolle y coloque a baño María para que se mantengan calientes."
            ],
            "notes": "Continúa en página 244 con la preparación del relleno y servido."
        }
    ]
}

# Page 244
pages["page_244"] = {
    "page": "244",
    "file": "recetario _244.jpg",
    "model": "gemini-3.8-flash",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "CREPAS RELLENAS DE MANZANA",
            "normalized_title": "crepas rellenas de manzana",
            "is_continuation": True,
            "ingredients": [],
            "steps": [
                "Derrita la margarina, agregue la manzana, azúcar y canela. Cocine a fuego mediano hasta que espese y haya cambiado el color de la manzana.",
                "Para servir coloque en un azafate las crepas calientes rellenas y espolvoree con la mezcla de azúcar con canela.",
                "Da para 15 porciones."
            ],
            "notes": "Continuación de la página 243."
        }
    ]
}

# Page 245
pages["page_245"] = {
    "page": "245",
    "file": "recetario _245.jpg",
    "model": "gemini-3.8-flash",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "ENSALADA DE PEPINO ESPECIAL",
            "normalized_title": "ensalada de pepino especial",
            "is_continuation": False,
            "ingredients": [
                "4 Pepinos cortados en luna (sin semilla)",
                "3 Cebollas cortadas en gajos",
                "2 Chiles pimientos cortados en tiritas pequeñas",
                "2 Huevos duros bien picaditos",
                "1/2 Taza de vinagre",
                "1/4 Taza de agua",
                "1 Taza de crema",
                "1/2 Taza de mayonesa",
                "Sal y pimienta al gusto",
                "Perejil picado"
            ],
            "steps": [
                "Se colocan los pepinos cortados en luna en una vinagreta hecha con el vinagre, agua, sal y pimienta.",
                "Allí mismo se vierte la cebolla con el chile pimiento, el cual se ha pasado previamente por agua hirviendo.",
                "Se deja reposar allí por 2 horas para agarrar sabor.",
                "Por aparte se une la mayonesa, crema, huevos duros bien picaditos, perejil picado, sal y pimienta.",
                "En esta mezcla cremosa se vierten los pepinos y vegetales escurridos.",
                "Se sirve bien fría."
            ],
            "notes": "Edith's Kitchen."
        }
    ]
}

# Page 246
pages["page_246"] = {
    "page": "246",
    "file": "recetario _246.jpg",
    "model": "gemini-3.8-flash",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "PASTEL ESPONJOSO DE FRUTAS",
            "normalized_title": "pastel esponjoso de frutas",
            "is_continuation": False,
            "ingredients": [
                "4 Huevos enteros",
                "1/2 Taza más una cucharada de azúcar",
                "1/2 Cucharadita de vainilla",
                "1 Taza menos 2 cucharadas de harina cernida",
                "7 Cucharadas de mantequilla derretida",
                "Gelatina sin sabor",
                "Crema pastelera (para relleno)",
                "Almíbar de azúcar, canela y agua con cáscara de limón o naranja",
                "Frutas escurridas variadas (melocotón, guindas, higos, piña)",
                "Jalea de albaricoque",
                "Almendra fileteada tostada"
            ],
            "steps": [
                "Para la masa, se mezcla en un bowl caliente los huevos enteros, el azúcar y la vainilla (o a baño María por 5 minutos) batiendo hasta espumar mucho.",
                "Agregar la harina poco a poco en forma envolvente y por último la mantequilla refrescada, con mucho cuidado a que no se quede toda en el fondo.",
                "Se hornea en molde bien engrasado y enharinado (con redondel de papel encerado) a 350 grados por 30 a 35 minutos. Se debe sacar inmediatamente del molde.",
                "Se moja el pastel con el almíbar cítrico y se rellena de crema pastelera.",
                "Se decora con las frutas por encima y a los lados con la almendra fileteada tostada.",
                "Glasear las frutas con jalea de albaricoque disuelta en agua y gelatina sin sabor."
            ],
            "notes": "Edith's Kitchen."
        }
    ]
}

# Page 247
pages["page_247"] = {
    "page": "247",
    "file": "recetario _247.jpg",
    "model": "gemini-3.8-flash",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "PIE DE PUERRO",
            "normalized_title": "pie de puerro",
            "is_continuation": False,
            "ingredients": [
                "1 Masa de pie (2 barras de margarina, 2 tazas de harina, pizca de sal y azúcar, agua helada, queso parmesano)",
                "3 Tazas de puerro tiernos y en rodaja",
                "3 Huevos bien batidos",
                "1/2 Taza de crema",
                "1/2 o 1 Taza de queso suizo o pecorino",
                "2 Cucharadas de mantequilla",
                "Sal y pimienta"
            ],
            "steps": [
                "Se fríe el puerro en la mantequilla hasta suavizar durante 3 o 4 minutos, y se le agrega la crema, sazonando al gusto.",
                "Por aparte se baten bien los huevos, se le mezcla el queso suizo o pecorino y se sazona.",
                "Esta mezcla de queso y huevo se une a la preparación anterior de puerro.",
                "Se forra el molde de pie con la masa preparada, se vierte la mezcla y se hornea a 375° por 25 a 30 minutos."
            ],
            "notes": "Edith's Kitchen."
        }
    ]
}

# Page 248
pages["page_248"] = {
    "page": "248",
    "file": "recetario _248.jpg",
    "model": "gemini-3.8-flash",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "CREMA PASTELERA RAPIDA",
            "normalized_title": "crema pastelera rapida",
            "is_continuation": False,
            "ingredients": [
                "1/2 Litro de leche",
                "2 Yemas de huevo",
                "4 Cucharadas de maicena",
                "1 Taza de azúcar cernida",
                "1/2 Vaso de crema",
                "2 Onzas de mantequilla",
                "1 Cucharadita de vainilla",
                "1 Raja de canela",
                "Pizca de sal",
                "Amareto o Kalúa al gusto"
            ],
            "steps": [
                "Licuar todo (leche, yemas, maicena, azúcar, pizca de sal y licor) excepto la vainilla, mantequilla y crema.",
                "Poner a cocinar con la raja de canela hasta que espese.",
                "Retirar del fuego, retirar la canela y agregar la vainilla, mantequilla y crema.",
                "Batir vigorosamente para que quede bien cremosa."
            ],
            "notes": "Edith's Kitchen."
        }
    ]
}

# Page 249
pages["page_249"] = {
    "page": "249",
    "file": "recetario _249.jpg",
    "model": "gemini-3.8-flash",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "BRAZO GITANO",
            "normalized_title": "brazo gitano",
            "is_continuation": False,
            "ingredients": [
                "7 Huevos separados",
                "1 Taza de azúcar",
                "1/2 Taza de harina cernida",
                "Pliego de papel parafinado",
                "Limpiador rociado de azúcar glass",
                "1 Lata de cajeta de leche",
                "Variación chocolate: 1/4 taza de cocoa amarga con 2 cucharaditas de ron"
            ],
            "steps": [
                "Separe los huevos. Bata las claras con un poquito de sal y agua para que crezcan; cuando estén a punto de nieve, agregue las yemas, siga batiendo, luego el azúcar y por último el harina cernida.",
                "Mezcle en forma envolvente, y si es con batidora, en la velocidad más baja.",
                "Engrase y enharine un molde grande para brazo gitano utilizando papel parafinado.",
                "Hornee a 350° por 15 minutos.",
                "Prepare el limpiador rociado de azúcar glass, coloque allí la masa recién horneada, retire el papel, úntela con la cajeta y enrolle con ayuda del limpiador.",
                "Guarde en el refrigerador por media hora.",
                "Variaciones: Se puede rellenar con crema pastelera, o con helado decorando con crema batida encima."
            ],
            "notes": "Edith's Kitchen."
        }
    ]
}

# Page 250
pages["page_250"] = {
    "page": "250",
    "file": "recetario _250.jpg",
    "model": "gemini-3.8-flash",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "CREPAS DE POLENTA CON POLLO Y BROCOLI",
            "normalized_title": "crepas de polenta con pollo y brocoli",
            "is_continuation": False,
            "ingredients": [
                "1/4 Taza de polenta (harina cornmeal)",
                "1/2 Taza de agua caliente",
                "1 Taza de leche tibia",
                "2 Huevos",
                "1/2 a 3/4 Taza de harina cernida",
                "1 Cucharada de mantequilla derretida o aceite vegetal",
                "Sal y pimienta",
                "1 1/2 Taza de pollo desmenuzado y cocido (para el relleno)",
                "1 Taza de brocoli cocido y picado (para el relleno)",
                "1 Cebolla picada fina (para el relleno)",
                "2 Dientes de ajo picados (para el relleno)",
                "1 Taza de leche, 1 cucharada de mantequilla, 1 cucharada de harina (para salsa blanca)",
                "Vino blanco (para la salsa blanca)",
                "1 Taza de queso cheddar rallado"
            ],
            "steps": [
                "Prepare las crepas mezclando primero la polenta con el agua hirviendo y dejando reposar por 10 minutos.",
                "Agregue a la polenta la leche tibia, los huevos, la harina, mantequilla derretida o aceite, sal y pimienta, mezclando hasta formar una masa suave de crepas.",
                "Para el relleno: preparar una salsa blanca especial con la mantequilla, harina, leche, un toque de vino y queso.",
                "Mezclar a la salsa blanca el pollo cocido desmenuzado, el brócoli picado y un poco de queso.",
                "Haga las crepas en una sartén ligeramente untada con mantequilla.",
                "Rellene cada crepa con la mezcla de pollo y brócoli, acomódelas en un pyrex, rocíe con más salsa blanca y queso cheddar rallado por encima.",
                "Hornee a 350° de 10 a 15 minutos hasta gratinar."
            ],
            "notes": "Edith's Kitchen."
        }
    ]
}

# Page 251
pages["page_251"] = {
    "page": "251",
    "file": "recetario _251.jpg",
    "model": "gemini-3.8-flash",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "MASA DE PIE DULCE",
            "normalized_title": "masa de pie dulce",
            "is_continuation": False,
            "ingredients": [
                "2 Tazas de harina",
                "1/2 Taza de mantequilla fría",
                "4 Yemas",
                "5 Cucharadas de azúcar",
                "1/2 Cucharadita de sal",
                "6 a 7 Cucharadas de agua fría congelada"
            ],
            "steps": [
                "Hacer una fuente con el harina en la mesa de trabajo.",
                "Agregar el resto de ingredientes al centro (mantequilla fría cortada, yemas, azúcar, sal y agua helada).",
                "Ir uniendo todo poco a poco con las puntas de los dedos, sin trabajarla mucho para que quede quebradiza.",
                "Poner a reposar en la refrigeradora envuelta en plástico por 1 hora.",
                "Se sirve o utiliza fría."
            ],
            "notes": "Edith's Kitchen."
        }
    ]
}

# Page 252
pages["page_252"] = {
    "page": "252",
    "file": "recetario _252.jpg",
    "model": "gemini-3.8-flash",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "PASTEL DE CHOCOLATE ESPECIAL",
            "normalized_title": "pastel de chocolate especial",
            "is_continuation": False,
            "ingredients": [
                "2 Tazas más 4 cucharadas de harina",
                "1 3/4 Tazas de azúcar",
                "1/4 Taza de cocoa en polvo",
                "3/4 Cucharadita de sal",
                "1 1/2 Cucharadita de royal",
                "1 Cucharadita de bicarbonato",
                "3 Huevos",
                "1 Cucharadita de vainilla",
                "3/4 Taza de leche",
                "1/2 Taza de aceite",
                "Guindas para decorar (con miel espesada con maicena)",
                "Crema chantilly (hecha con azúcar glass y vainilla)",
                "Galleta de chocolate quebrada"
            ],
            "steps": [
                "Unir ingredientes secos (harina, azúcar, cocoa, sal, royal, bicarbonato).",
                "Combinar con los ingredientes líquidos (huevos, vainilla, leche, aceite).",
                "Batir con batidora a velocidad media hasta homogenizar bien.",
                "Colocar en molde engrasado y enharinado con redondel de papel encerado.",
                "Hornear por 35 minutos hasta que salga limpio el palillo a 350° grados.",
                "Decorar con crema chantilly, galleta de chocolate quebrada y guindas abrillantadas."
            ],
            "notes": "Edith's Kitchen."
        }
    ]
}

# Page 253
pages["page_253"] = {
    "page": "253",
    "file": "recetario _253.jpg",
    "model": "gemini-3.8-flash",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "FUSILLI CON SALSA DE CHILE PIMIENTO",
            "normalized_title": "fusilli con salsa de chile pimiento",
            "is_continuation": False,
            "ingredients": [
                "1 Libra de fusilli",
                "4 Onzas de queso cheddar",
                "4 Onzas de queso mozzarella",
                "Polvo paprika o pimentón español",
                "2 Latas de chile pimiento morrón",
                "1 Lata de leche evaporada",
                "2 Onzas de margarina",
                "Sal y aceite para cocer la pasta"
            ],
            "steps": [
                "Cocine la pasta con sal y un poco de aceite; escurrir.",
                "En un trasto a baño María coloque la margarina y el queso cheddar y mozzarella.",
                "Cuando esté derretido el queso, añada la leche evaporada previamente licuada con los chiles pimientos.",
                "Añada la sal y la paprika al gusto.",
                "En un pyrex engrasado coloque los macarrones fusilli y vierta encima la salsa.",
                "Hornear a 350° hasta que la salsa hierva y dore ligeramente."
            ],
            "notes": "Edith's Kitchen."
        }
    ]
}

# Page 254
pages["page_254"] = {
    "page": "254",
    "file": "recetario _254.jpg",
    "model": "gemini-3.8-flash",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "MASA BASICA DE FRITURAS DULCES",
            "normalized_title": "masa basica de frituras dulces",
            "is_continuation": False,
            "ingredients": [
                "3/4 Taza de harina",
                "1 Cucharada de azúcar",
                "1 Cucharada de mantequilla derretida",
                "1 Taza de agua tibia",
                "1 Pizca de sal",
                "1 Huevo separado",
                "Aceite para freír en grasa profunda"
            ],
            "steps": [
                "Cernir juntos harina y azúcar.",
                "Añadir mantequilla derretida y agua tibia, hasta hacer una pasta suave.",
                "Añadir sal, batir aparte la clara a punto de nieve, y agregar en forma envolvente luego de agregar la yema.",
                "Forrar con esta pasta las frutas elegidas (como rodajas de manzana).",
                "Freír en grasa profunda bien caliente hasta que doren."
            ],
            "notes": "Edith's Kitchen."
        }
    ]
}

# Page 255
pages["page_255"] = {
    "page": "255",
    "file": "recetario _255.jpg",
    "model": "gemini-3.8-flash",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "FRITURAS DE MANZANA O BANANO",
            "normalized_title": "frituras de manzana o banano",
            "is_continuation": False,
            "ingredients": [
                "1 Receta de masa de choux",
                "Manzanas o bananos tajados con azúcar y limón",
                "Aceite para freír en grasa profunda"
            ],
            "steps": [
                "Tajear las manzanas o bananos y macerar con azúcar y unas gotas de limón.",
                "Envolver las rebanadas de fruta en la masa de choux.",
                "Freír en grasa profunda caliente hasta que doren parejo y esponjen.",
                "Escurrir y servir calientes."
            ],
            "notes": "Edith's Kitchen."
        }
    ]
}

# Write page files
for page_key, page_data in pages.items():
    file_path = PAGES_DIR / f"{page_key}.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(page_data, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"Wrote {file_path}")

print("Batch 29 pages generated successfully.")
