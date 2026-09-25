import json
from pathlib import Path

PAGES_DIR = Path("cache/pages")
PAGES_DIR.mkdir(parents=True, exist_ok=True)

pages = {}

# Page 256
pages["page_256"] = {
    "page": "256",
    "file": "recetario _256.jpg",
    "model": "gemini-3.8-flash",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "AZUCARADO DE MANTEQUILLA",
            "normalized_title": "azucarado de mantequilla",
            "is_continuation": False,
            "ingredients": [
                "4 onzas de margarina",
                "1 pizca de sal",
                "1 libra de azúcar glass cernida",
                "2 yemas de huevo",
                "1 cucharadita de vainilla",
                "2 cucharadas de leche caliente"
            ],
            "steps": [
                "Cremar la margarina con la sal y agregar alternando con la leche el azúcar glass.",
                "Por último se agregan las yemas y la vainilla batiendo a que quede suave."
            ],
            "notes": ""
        },
        {
            "kind": "recipe",
            "title": "COCO RALLADO DE COLOR",
            "normalized_title": "coco rallado de color",
            "is_continuation": False,
            "ingredients": [
                "1/2 cucharadita de agua",
                "Colorante vegetal líquido (unas gotas)",
                "1 1/2 taza de coco rallado deshidratado"
            ],
            "steps": [
                "En un tazón pequeño mezclar el agua con el colorante vegetal deseado (pocas gotas).",
                "Agregar el coco y mezclar bien con un tenedor hasta que tome un color parejo. Dejar secar sobre papel encerado."
            ],
            "notes": ""
        },
        {
            "kind": "recipe",
            "title": "COCO TOSTADO",
            "normalized_title": "coco tostado",
            "is_continuation": False,
            "ingredients": [
                "Coco rallado"
            ],
            "steps": [
                "Extender el coco en latas de hornear galletas.",
                "Hornear a 175°C de 7 a 12 minutos o hasta que esté ligeramente dorado, moviendo ocasionalmente."
            ],
            "notes": ""
        }
    ]
}

# Page 257
pages["page_257"] = {
    "page": "257",
    "file": "recetario _257.jpg",
    "model": "gemini-3.8-flash",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "PASTEL DE ZANAHORIA",
            "normalized_title": "pastel de zanahoria",
            "is_continuation": False,
            "ingredients": [
                "2 tazas de azúcar",
                "1 taza de aceite",
                "4 huevos",
                "1 cucharadita de sal",
                "2 cucharaditas de bicarbonato",
                "1 cucharadita de canela en polvo",
                "3 tazas de zanahoria rallada cruda",
                "2 tazas de harina",
                "1 taza de nueces picadas",
                "1 cucharadita de polvo de hornear (Royal)",
                "Forro:",
                "8 onzas de queso crema",
                "2 cucharaditas de vainilla blanca",
                "2 tazas de azúcar glass",
                "6 cucharadas de mantequilla"
            ],
            "steps": [
                "Batir el azúcar con el aceite, agregar los huevos uno a uno batiendo bien.",
                "Cernir los ingredientes secos: harina, sal, bicarbonato, canela y Royal; incorporar a la mezcla anterior.",
                "Agregar la zanahoria rallada y las nueces picadas.",
                "Verter en molde engrasado y enharinado. Hornear a 350°F por 30 a 40 minutos.",
                "Para el forro: batir el queso crema con la mantequilla, vainilla blanca y azúcar glass hasta obtener una consistencia cremosa y suave. Decorar el pastel una vez frío."
            ],
            "notes": "Edith's Kitchen."
        }
    ]
}

# Page 258
pages["page_258"] = {
    "page": "258",
    "file": "recetario _258.jpg",
    "model": "gemini-3.8-flash",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "PIE DE POLLO",
            "normalized_title": "pie de pollo",
            "is_continuation": False,
            "ingredients": [
                "1 receta de masa de pie doble",
                "3 pechugas de pollo cocidas y desmenuzadas",
                "2 cucharadas de tomate picado",
                "2 cucharadas de mantequilla",
                "1 zanahoria cocida cortada en cuadritos",
                "1 taza de arvejas cocidas",
                "3 cucharadas de cebolla picada",
                "1/2 taza de chile pimiento picado",
                "2 huevos batidos",
                "1 taza de crema",
                "Sal y pimienta al gusto"
            ],
            "steps": [
                "Freír en mantequilla la cebolla, tomate y chile pimiento.",
                "Agregar el pollo desmenuzado, la zanahoria y las arvejas. Sazonar con sal y pimienta.",
                "Añadir la crema y los huevos batidos, mezclando bien.",
                "Forrar un molde de pie con la mitad de la masa, rellenar con la mezcla de pollo y cubrir con el resto de la masa (o tiras enrejadas).",
                "Hornear a 350°F por 20 a 30 minutos hasta que la masa esté dorada."
            ],
            "notes": "Edith's Kitchen."
        }
    ]
}

# Page 259
pages["page_259"] = {
    "page": "259",
    "file": "recetario _259.jpg",
    "model": "gemini-3.8-flash",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "TRES LECHES",
            "normalized_title": "tres leches",
            "is_continuation": False,
            "ingredients": [
                "Masa:",
                "9 huevos (separadas claras y yemas)",
                "2 tazas de azúcar",
                "2 tazas de harina de trigo cernida",
                "1/2 taza de leche líquida",
                "1 cucharadita de polvo de hornear",
                "1 cucharadita de vainilla",
                "Baño de tres leches:",
                "1 lata de leche condensada (14 oz)",
                "1 lata de leche evaporada (14 oz)",
                "1 vaso de crema pura de vaca",
                "1 cucharadita de vainilla",
                "2 cucharadas de licor (ron o brandy)"
            ],
            "steps": [
                "Batir las claras a punto de nieve e incorporar poco a poco el azúcar.",
                "Añadir las yemas una a una batiendo constantemente.",
                "Incorporar con espátula la harina con el polvo de hornear alternando con la leche y la vainilla con movimientos envolventes.",
                "Verter en molde engrasado y enharinado. Hornear a 350°F (180°C) durante 30 minutos.",
                "Mezclar los ingredientes del baño: leche condensada, leche evaporada, crema, vainilla y licor.",
                "Pinchar el pastel caliente o tibio con un tenedor y bañar con la mezcla de tres leches. Refrigerar."
            ],
            "notes": "Chef Violeta Ortiz."
        }
    ]
}

# Page 260
pages["page_260"] = {
    "page": "260",
    "file": "recetario _260.jpg",
    "model": "gemini-3.8-flash",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "GALLETAS A DOS TONOS",
            "normalized_title": "galletas a dos tonos",
            "is_continuation": False,
            "ingredients": [
                "1/2 taza de mantequilla",
                "1 taza de azúcar morena",
                "1 huevo",
                "1/2 cucharadita de vainilla",
                "1 3/4 tazas de harina",
                "1/2 cucharadita de bicarbonato",
                "3/4 cucharadita de sal",
                "1/2 onza de chocolate amargo derretido"
            ],
            "steps": [
                "Cremar la mantequilla con el azúcar morena, agregar el huevo y la vainilla.",
                "Cernir la harina con el bicarbonato y la sal; agregar a la mezcla.",
                "Dividir la masa en dos partes. A una parte agregarle el chocolate amargo derretido.",
                "Extender ambas masas por separado formando rectángulos iguales, colocar una sobre la otra y enrollar en forma de cilindro.",
                "Refrigerar hasta que esté firme. Cortar en rodajas finas y colocar en latas engrasadas.",
                "Hornear a 400°F durante 8 a 10 minutos."
            ],
            "notes": ""
        }
    ]
}

# Page 261
pages["page_261"] = {
    "page": "261",
    "file": "recetario _261.jpg",
    "model": "gemini-3.8-flash",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "GALLETAS DE MANTEQUILLA Y ALMENDRA",
            "normalized_title": "galletas de mantequilla y almendra",
            "is_continuation": False,
            "ingredients": [
                "4 onzas de mantequilla",
                "2 onzas de azúcar glass",
                "1 yema de huevo",
                "6 onzas de harina",
                "2 onzas de almendras picadas tostadas",
                "1/4 cucharadita de polvo de hornear",
                "1/2 cucharadita de bicarbonato",
                "2 cucharadas de ajonjolí tostado para decorar"
            ],
            "steps": [
                "Batir la mantequilla con el azúcar glass hasta estar cremosa. Agregar la yema.",
                "Incorporar la harina cernida con el polvo de hornear y bicarbonato.",
                "Agregar las almendras picadas y amasar ligeramente.",
                "Formar bolitas, aplanar y pasar por el ajonjolí tostado.",
                "Colocar en latas para hornear y hornear a 180°C por 20 minutos."
            ],
            "notes": ""
        }
    ]
}

# Page 262
pages["page_262"] = {
    "page": "262",
    "file": "recetario _262.jpg",
    "model": "gemini-3.8-flash",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "PASTEL DE MANTEQUILLA",
            "normalized_title": "pastel de mantequilla",
            "is_continuation": False,
            "ingredients": [
                "3 tazas de harina",
                "1 3/4 tazas de azúcar",
                "5 onzas de mantequilla pura sin sal",
                "2 huevos",
                "1 pizca de sal",
                "2 1/2 cucharaditas de polvo de hornear",
                "1 1/4 taza de leche",
                "1/2 taza de pasas (opcional)"
            ],
            "steps": [
                "Batir la mantequilla con el azúcar hasta que esté bien cremosa y blanca.",
                "Agregar los huevos uno a uno sin dejar de batir.",
                "Cernir la harina con el polvo de hornear y la sal; agregar a la mezcla alternando con la leche.",
                "Envolver las pasas previamente enharinadas.",
                "Verter en molde engrasado y hornear a 175°C por 50 a 60 minutos."
            ],
            "notes": ""
        }
    ]
}

# Page 263
pages["page_263"] = {
    "page": "263",
    "file": "recetario _263.jpg",
    "model": "gemini-3.8-flash",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "CREMA DE ALMENDRA",
            "normalized_title": "crema de almendra",
            "is_continuation": False,
            "ingredients": [
                "1 yema de huevo",
                "1/3 taza de azúcar",
                "1 1/2 tazas de leche",
                "2 cucharadas de maicena",
                "1 cucharadita de esencia de almendra",
                "1/4 taza de almendra fileteada tostada"
            ],
            "steps": [
                "Disolver la maicena en un poco de leche fría.",
                "En una olla mezclar el resto de la leche con el azúcar y la yema batida.",
                "Agregar la maicena disuelta y cocinar a fuego medio moviendo constantemente durante 3 minutos o hasta que espese.",
                "Retirar del fuego, añadir la esencia de almendra y las almendras fileteadas. Dejar enfriar cubierta con plástico."
            ],
            "notes": ""
        }
    ]
}

# Page 264
pages["page_264"] = {
    "page": "264",
    "file": "recetario _264.jpg",
    "model": "gemini-3.8-flash",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "PRETZELZ DE ALMENDRA",
            "normalized_title": "pretzelz de almendra",
            "is_continuation": False,
            "ingredients": [
                "1 taza de mantequilla",
                "1 taza de azúcar",
                "3 yemas de huevo",
                "1 taza de almendras molidas con cáscara",
                "Ralladura de media naranja",
                "2 a 3 tazas de harina"
            ],
            "steps": [
                "Batir la mantequilla con el azúcar, agregar las yemas una a una.",
                "Incorporar la ralladura de naranja y las almendras molidas.",
                "Agregar la harina poco a poco hasta formar una masa suave pero manejable.",
                "Refrigerar la masa durante 2 horas.",
                "Tomar porciones de masa, formar tiras cilíndricas delgadas y dar forma de pretzeles.",
                "Colocar en latas de hornear y hornear a 350°F por 15 minutos."
            ],
            "notes": ""
        }
    ]
}

# Page 265
pages["page_265"] = {
    "page": "265",
    "file": "recetario _265.jpg",
    "model": "gemini-3.8-flash",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "REGALOS DE AZÚCAR",
            "normalized_title": "regalos de azucar",
            "is_continuation": False,
            "ingredients": [
                "2 tazas de harina",
                "3/4 cucharadita de sal",
                "1/2 cucharadita de polvo de hornear",
                "1/2 cucharadita de jengibre molido",
                "3/4 cucharadita de canela molida",
                "1/2 cucharadita de pimienta dulce molida",
                "1/4 cucharadita de nuez moscada",
                "5 onzas de mantequilla",
                "2/3 taza de azúcar morena",
                "1/2 cucharadita de vainilla",
                "1 huevo",
                "Glaseado / Decoración:",
                "3 tazas de azúcar glass",
                "1/4 taza de agua tibia",
                "Colorantes vegetales rojo y verde"
            ],
            "steps": [
                "Cernir la harina con la sal, polvo de hornear y especias (jengibre, canela, pimienta, nuez moscada).",
                "Batir la mantequilla con el azúcar morena, agregar el huevo y la vainilla.",
                "Incorporar los ingredientes secos formando una masa compacta. Envolver en plástico y refrigerar 1 hora.",
                "Extender la masa a 1/2 cm de grosor y cortar en cuadrados simulando paquetitos o regalos.",
                "Hornear a 350°F por 8 a 12 minutos. Dejar enfriar.",
                "Preparar el glaseado mezclando azúcar glass con el agua, separar y pintar de colores para decorar como cintas y lazos de regalo."
            ],
            "notes": ""
        }
    ]
}

# Page 266
pages["page_266"] = {
    "page": "266",
    "file": "recetario _266.jpg",
    "model": "gemini-3.8-flash",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "MASA DE PIE",
            "normalized_title": "masa de pie",
            "is_continuation": False,
            "ingredients": [
                "4 barras de margarina bien fría",
                "2 tazas de harina",
                "1/4 taza de queso parmesano rallado",
                "Agua con hielo (cantidad necesaria)",
                "Clara, yema o leche para brochear (dar brillo)"
            ],
            "steps": [
                "Cortar la margarina fría en cubitos e incorporar a la harina y queso parmesano con estribo o tenedor hasta obtener textura arenosa.",
                "Agregar agua con hielo por cucharadas hasta unir la masa sin amasar en exceso.",
                "Extender en el molde para pie, rellenar y barnizar con clara, yema o leche para que dore y tenga brillo."
            ],
            "notes": ""
        }
    ]
}

# Page 267
pages["page_267"] = {
    "page": "267",
    "file": "recetario _267.jpg",
    "model": "gemini-3.8-flash",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "QUICHE LORRAINE",
            "normalized_title": "quiche lorraine",
            "is_continuation": False,
            "ingredients": [
                "1 masa de pie sin hornear",
                "1/2 libra de tocino frito y picado",
                "1/2 taza de cebolla finamente picada",
                "1/2 libra de queso suizo o gruyere rallado",
                "3 huevos grandes batidos",
                "1 taza de crema agria",
                "1/2 taza de leche con 1 cucharada de maicena disuelta",
                "1/2 cucharadita de sal",
                "Nuez moscada o pimienta de cayena al gusto"
            ],
            "steps": [
                "Freír el tocino hasta dorar y escurrir; en la misma grasa sofreír la cebolla picada.",
                "En el fondo de la masa de pie colocar el tocino, cebolla y el queso rallado.",
                "Batir los huevos con la crema agria, la leche con maicena, sal y nuez moscada.",
                "Verter la mezcla líquida sobre el queso y tocino.",
                "Hornear a 350°F por aproximadamente 30 minutos o hasta que cuaje y dore la superficie."
            ],
            "notes": ""
        }
    ]
}

# Page 268
pages["page_268"] = {
    "page": "268",
    "file": "recetario _268.jpg",
    "model": "gemini-3.8-flash",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "Tacos al Pastor",
            "normalized_title": "tacos al pastor",
            "is_continuation": False,
            "ingredients": [
                "1 cucharada de ajo picado",
                "100 gramos de cebolla",
                "2 chiles guajillos remojados y limpios",
                "1 cucharada de azúcar",
                "50 cc de jugo de limón",
                "50 cc de jugo de naranja",
                "100 cc de vinagre de manzana",
                "1 cucharada de orégano",
                "1 cucharada de achiote en polvo (opcional)",
                "100 cc de jugo de piña",
                "Sal y pimienta al gusto",
                "Carne de cerdo cortada en bisteces delgados"
            ],
            "steps": [
                "Licuar todos los ingredientes del adobo: ajo, cebolla, chiles guajillo, azúcar, jugos de limón, naranja y piña, vinagre, orégano, achiote, sal y pimienta.",
                "Marinar la carne de cerdo en el adobo durante al menos 2 a 4 horas o toda la noche.",
                "Cocinar la carne asada o en sartén bien caliente hasta que esté dorada, picar finamente y servir en tortillas con cebolla, cilantro y piña."
            ],
            "notes": ""
        }
    ]
}

# Page 269
pages["page_269"] = {
    "page": "269",
    "file": "recetario _269.jpg",
    "model": "gemini-3.8-flash",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "Nachos o Papas Supreme",
            "normalized_title": "nachos o papas supreme",
            "is_continuation": False,
            "ingredients": [
                "Totopos de maíz o papas fritas",
                "Queso spread derretido",
                "Carne molida sazonada cocida",
                "Tomate picado en cubitos",
                "Tallos de cebollín picados",
                "Crema agria"
            ],
            "steps": [
                "Colocar una base de totopos o papas fritas en una bandeja.",
                "Bañar con el queso spread derretido caliente.",
                "Distribuir encima la carne molida sazonada, el tomate en cubitos y los tallos de cebollín picados.",
                "Coronar con cucharadas de crema agria antes de servir."
            ],
            "notes": ""
        },
        {
            "kind": "recipe",
            "title": "Caldo Tlalpeño",
            "normalized_title": "caldo tlalpeno",
            "is_continuation": False,
            "ingredients": [
                "Pollo cocido y desmenuzado en su caldo",
                "Arroz cocido con arvejas, cilantro y cebolla",
                "Ajo picado",
                "Cebolla cortada en gajos",
                "Clavos de olor",
                "Cilantro picado",
                "Aguacate en cubitos",
                "Cebollín picado"
            ],
            "steps": [
                "Preparar el caldo de pollo sazonado con cebolla en gajos, ajo picado y clavos de olor.",
                "En cada plato hondo servir una porción de arroz cocido con arvejas y pollo desmenuzado.",
                "Bañar con el caldo de pollo bien caliente.",
                "Decorar encima con aguacate picado, cilantro fresco picado y cebollín."
            ],
            "notes": ""
        }
    ]
}

# Page 270
pages["page_270"] = {
    "page": "270",
    "file": "recetario _270.jpg",
    "model": "gemini-3.8-flash",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "Frijol Colorado",
            "normalized_title": "frijol colorado",
            "is_continuation": False,
            "ingredients": [
                "Frijol colorado",
                "2 chiles pimientos",
                "7 miltomates",
                "4 tomates",
                "3 dientes de ajo",
                "2 cebollas",
                "Pepita tostada y molida",
                "Tomillo y laurel",
                "Sal al gusto"
            ],
            "steps": [
                "Poner a cocer los frijoles colorados con tomillo, laurel, ajo y cebolla.",
                "Asar o cocer los tomates, miltomates, chiles pimientos, cebolla y ajos; licuar finamente con la pepita tostada para formar el recado.",
                "Agregar el recado licuado a los frijoles cocidos y dejar hervir a fuego lento para que espese e integren los sabores."
            ],
            "notes": ""
        },
        {
            "kind": "recipe",
            "title": "Chimichurri",
            "normalized_title": "chimichurri",
            "is_continuation": False,
            "ingredients": [
                "1 manojo de cilantro fresco picado",
                "Hojas de albahaca verde picadas",
                "Aceite de oliva o vegetal",
                "4 cebollas grandes finamente picadas",
                "3 cabezas de ajo peladas y picadas",
                "Vinagre de manzana",
                "Vino blanco o tinto",
                "Sal y pimienta al gusto"
            ],
            "steps": [
                "Picar finamente el cilantro, albahaca, ajos y cebollas.",
                "Mezclar en un tazón hondo o frasco con abundante aceite de oliva.",
                "Agregar vinagre de manzana y vino al gusto.",
                "Sazonar con sal y pimienta recién molida. Dejar reposar para que se concentren los aromas."
            ],
            "notes": ""
        }
    ]
}

# Page 271
pages["page_271"] = {
    "page": "271",
    "file": "recetario _271.jpg",
    "model": "gemini-3.8-flash",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "Burrito",
            "normalized_title": "burrito",
            "is_continuation": False,
            "ingredients": [
                "Tortillas de harina grandes",
                "Carne molida preparada con salsa",
                "Arroz blanco cocido",
                "Crema",
                "Queso rallado"
            ],
            "steps": [
                "Calentar las tortillas de harina hasta que estén suaves y flexibles.",
                "Colocar en el centro una capa de carne molida guisada con salsa y arroz blanco.",
                "Añadir crema y queso al gusto.",
                "Doblar los bordes laterales hacia adentro y enrollar firmemente formando el burrito."
            ],
            "notes": ""
        }
    ]
}

# Page 272
pages["page_272"] = {
    "page": "272",
    "file": "recetario _272.jpg",
    "model": "gemini-3.8-flash",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "Salsa Tártara",
            "normalized_title": "salsa tartara",
            "is_continuation": False,
            "ingredients": [
                "1 taza de mayonesa",
                "Jugo de 1 limón",
                "Pepinillos agridulces o salados picados finamente",
                "1 huevo duro finamente picado",
                "Alcaparras picadas",
                "1 cucharadita de mostaza",
                "Perejil fresco finamente picado"
            ],
            "steps": [
                "En un tazón mezclar la mayonesa con el jugo de limón y la mostaza.",
                "Incorporar los pepinillos, las alcaparras y el perejil picado.",
                "Agregar el huevo duro picado con cuidado para no deshacerlo por completo. Refrigerar antes de servir."
            ],
            "notes": ""
        },
        {
            "kind": "recipe",
            "title": "Hilachas",
            "normalized_title": "hilachas",
            "is_continuation": False,
            "ingredients": [
                "Carne de res para hilachas (falda o bolovique)",
                "Laurel y tomillo",
                "Papas pequeñas con cáscara (partidas)",
                "Salsa / Recado:",
                "6 tomates maduros",
                "1 chile pimiento",
                "8 miltomates",
                "2 dientes de ajo",
                "2 cebollas",
                "Sal, pimienta y comino"
            ],
            "steps": [
                "Cocinar la carne en olla de presión con agua, laurel, tomillo y sal hasta que esté muy suave; retirar y deshilachar la carne reservando el caldo.",
                "Asar o cocer los tomates, miltomates, chile pimiento, ajos y cebollas; licuar con un poco de caldo y sazonar con comino, sal y pimienta.",
                "En una olla colocar la salsa, añadir las papas pequeñas y cocinar hasta que estén tiernas.",
                "Incorporar la carne deshilachada y hervir todo junto a fuego suave hasta espesar."
            ],
            "notes": ""
        }
    ]
}

# Page 273
pages["page_273"] = {
    "page": "273",
    "file": "recetario _273.jpg",
    "model": "gemini-3.8-flash",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "Lasagna",
            "normalized_title": "lasagna",
            "is_continuation": False,
            "ingredients": [
                "Láminas de pasta para lasaña",
                "Carne molida de res",
                "Zanahoria picada finamente",
                "Salsa de tomate",
                "Nuez moscada",
                "Sal y pimienta",
                "Queso mozzarella rallado"
            ],
            "steps": [
                "Preparar la carne molida sofriéndola con zanahoria, sazonar con sal, pimienta, nuez moscada y mezclar con la salsa de tomate.",
                "Cocer las láminas de pasta según las instrucciones del paquete.",
                "En un pyrex colocar capas alternadas de pasta, salsa con carne y queso mozzarella.",
                "Terminar con abundante queso y hornear hasta que esté bien gratinada."
            ],
            "notes": ""
        }
    ]
}

# Page 274
pages["page_274"] = {
    "page": "274",
    "file": "recetario _274.jpg",
    "model": "gemini-3.8-flash",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "Pollo Guisado con Arroz",
            "normalized_title": "pollo guisado con arroz",
            "is_continuation": False,
            "ingredients": [
                "Piezas de pollo",
                "Chile pimiento",
                "Miltomate",
                "Tomate",
                "Laurel y tomillo",
                "Cebolla y ajo",
                "Sal y pimienta"
            ],
            "steps": [
                "Cocer o guisar las piezas de pollo con chile pimiento, miltomates, tomate, cebolla, ajo, laurel y tomillo.",
                "Cocinar a fuego lento hasta que el pollo esté tierno y la salsa espese.",
                "Acompañar y servir con arroz cocido."
            ],
            "notes": ""
        },
        {
            "kind": "recipe",
            "title": "Arroz Cocido",
            "normalized_title": "arroz cocido",
            "is_continuation": False,
            "ingredients": [
                "Arroz corriente",
                "Agua o caldo",
                "Aceite o mantequilla",
                "Sal al gusto"
            ],
            "steps": [
                "Lavar y sofreír el arroz con un poco de grasa, agregar el doble de líquido y sal.",
                "Tapar y cocinar a fuego bajo hasta secar y esponjar."
            ],
            "notes": ""
        }
    ]
}

# Page 275
pages["page_275"] = {
    "page": "275",
    "file": "recetario _275.jpg",
    "model": "gemini-3.8-flash",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "Crema Pastelera",
            "normalized_title": "crema pastelera",
            "is_continuation": False,
            "ingredients": [
                "1/2 litro de leche",
                "1 vaina de vainilla",
                "125 gramos de azúcar",
                "40 gramos de fécula de maíz",
                "4 yemas de huevo"
            ],
            "steps": [
                "Hervir la leche con la vaina de vainilla abierta; retirar del fuego y dejar infusionar.",
                "En un tazón batir las yemas de huevo con el azúcar hasta blanquear, luego incorporar la fécula de maíz.",
                "Colar la leche tibia sobre la mezcla de yemas batiendo constantemente.",
                "Regresar la preparación al fuego lento, batiendo continuamente con batidor de alambre hasta que espese y hierva 1 minuto.",
                "Retirar del fuego y dejar enfriar cubierta con papel film pegado a la superficie."
            ],
            "notes": ""
        }
    ]
}

# Page 276
pages["page_276"] = {
    "page": "276",
    "file": "recetario _276.jpg",
    "model": "gemini-3.8-flash",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "Turrón",
            "normalized_title": "turron",
            "is_continuation": False,
            "ingredients": [
                "1 taza de azúcar",
                "1/4 taza de agua para punto de hebra (o 3/4 taza de agua)",
                "1/2 onza de polvo de clara (merengue)"
            ],
            "steps": [
                "Poner el azúcar con el agua al fuego para hacer una miel a punto de hebra o bola suave.",
                "Batir el polvo de clara a velocidad alta hasta que forme picos firmes.",
                "Disminuir la velocidad e incorporar la miel caliente en forma de hilo continuo batiendo hasta obtener brillo y firmeza."
            ],
            "notes": ""
        }
    ]
}

# Page 277
pages["page_277"] = {
    "page": "277",
    "file": "recetario _277.jpg",
    "model": "gemini-3.8-flash",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "Cupcakes",
            "normalized_title": "cupcakes",
            "is_continuation": False,
            "ingredients": [
                "4 1/2 tazas de harina de fuerza",
                "2 1/2 cucharadas de levadura",
                "3/4 cucharada de sal",
                "1 taza + 2 cucharadas soperas de mantequilla a temperatura ambiente",
                "2 1/2 tazas de azúcar",
                "6 huevos grandes",
                "2 cucharadas de vainilla",
                "1 1/4 taza de leche"
            ],
            "steps": [
                "Cremar la mantequilla con el azúcar hasta que esponje.",
                "Añadir los huevos uno a uno, luego la vainilla.",
                "Cernir la harina con la levadura y la sal; agregar a la mezcla alternando con la leche.",
                "Repartir en moldes para cupcakes con capacillos y hornear a 350°F (180°C) hasta que al insertar un palillo salga limpio."
            ],
            "notes": ""
        },
        {
            "kind": "recipe",
            "title": "Butter Cream",
            "normalized_title": "butter cream",
            "is_continuation": False,
            "ingredients": [
                "6 tazas de azúcar glass",
                "1 taza de manteca vegetal",
                "4 cucharadas de leche",
                "2 cucharaditas de vainilla"
            ],
            "steps": [
                "Acremar la manteca vegetal en batidora.",
                "Agregar gradualmente el azúcar glass alternando con la leche y la vainilla.",
                "Batir a velocidad media-alta hasta que quede suave y esponjoso para decorar."
            ],
            "notes": ""
        }
    ]
}

# Page 278
pages["page_278"] = {
    "page": "278",
    "file": "recetario _278.jpg",
    "model": "gemini-3.8-flash",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "Quesadilla",
            "normalized_title": "quesadilla",
            "is_continuation": False,
            "ingredients": [
                "1/2 libra de mantequilla",
                "2 tazas de azúcar",
                "8 huevos",
                "1 taza de harina de trigo",
                "3 tazas de harina de arroz",
                "2 cucharaditas de polvo de hornear",
                "8 onzas de crema de leche",
                "4 onzas de queso seco rallado",
                "1/2 taza de leche",
                "Para decorar:",
                "1/2 taza de azúcar mezclada con 3 cucharadas de canela en polvo"
            ],
            "steps": [
                "Batir la mantequilla y el azúcar hasta que esté cremosa.",
                "Añadir uno a uno los huevos.",
                "Agregar las harinas y el polvo de hornear alternando con la leche.",
                "Luego agregamos la crema y el queso seco rallado.",
                "Verter en moldes y espolvorear por encima con la mezcla de azúcar y canela.",
                "Hornear a 350°F hasta que dore."
            ],
            "notes": ""
        }
    ]
}

# Page 279
pages["page_279"] = {
    "page": "279",
    "file": "recetario _279.jpg",
    "model": "gemini-3.8-flash",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "Cheesecake",
            "normalized_title": "cheesecake",
            "is_continuation": False,
            "ingredients": [
                "1/2 libra (250 gramos) de queso crema",
                "2 huevos",
                "1 cucharadita de vainilla",
                "1 taza de crema agria",
                "1 taza de azúcar"
            ],
            "steps": [
                "Acremar el queso crema con el azúcar hasta que esté completamente suave.",
                "Agregar los huevos uno a uno, la vainilla y la crema agria.",
                "Verter en molde y hornear a baño maría a 325°F hasta que cuaje."
            ],
            "notes": ""
        },
        {
            "kind": "recipe",
            "title": "Salsa Marinara",
            "normalized_title": "salsa marinara",
            "is_continuation": False,
            "ingredients": [
                "Tomate",
                "Cebolla",
                "Ajo",
                "Hierbas",
                "Aceite de oliva",
                "Sal y pimienta"
            ],
            "steps": [
                "Sofreír cebolla y ajo picados en aceite de oliva.",
                "Agregar tomates picados o triturados y hierbas aromáticas.",
                "Sazonar con sal y pimienta y dejar cocinar a fuego bajo hasta que espese."
            ],
            "notes": ""
        }
    ]
}

# Page 280
pages["page_280"] = {
    "page": "280",
    "file": "recetario _280.jpg",
    "model": "gemini-3.8-flash",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "Papas Horneadas",
            "normalized_title": "papas horneadas",
            "is_continuation": False,
            "ingredients": [
                "Papas cortadas en gajos",
                "Aceite de oliva",
                "Queso parmesano",
                "Sal al gusto",
                "Especias italianas",
                "Ajo en polvo",
                "Pimentón español"
            ],
            "steps": [
                "Reunir todos los ingredientes secos en un bol.",
                "Las papas bañarlas con el aceite de oliva, y luego pasarles o agregarles la mezcla seca.",
                "Colocar sobre papel aluminio en una bandeja para hornear.",
                "Hornear por 40 min. a 350°."
            ],
            "notes": ""
        }
    ]
}

# Page 281
pages["page_281"] = {
    "page": "281",
    "file": "recetario _281.jpg",
    "model": "gemini-3.8-flash",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "Ensalada Fresas",
            "normalized_title": "ensalada fresas",
            "is_continuation": False,
            "ingredients": [
                "Lechuga colocha verde y morada",
                "Fresas cortadas",
                "Queso fresco",
                "Nueces, pasas",
                "Manzana",
                "Aliño:",
                "Aceite de oliva",
                "Pimienta blanca",
                "Limón",
                "Sal de hierbas",
                "1 jugo de naranja (opcional)"
            ],
            "steps": [
                "Mezclar las lechugas, fresas, queso fresco, nueces, pasas y manzana.",
                "Para el aliño: licuar el aceite de oliva, pimienta blanca, limón, sal de hierbas y jugo de naranja.",
                "Colocar el aliño sobre la ensalada."
            ],
            "notes": "Categoría manuscrita: Cena."
        }
    ]
}

# Page 282
pages["page_282"] = {
    "page": "282",
    "file": "recetario _282.jpg",
    "model": "gemini-3.8-flash",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "Batido Verde",
            "normalized_title": "batido verde",
            "is_continuation": False,
            "ingredients": [
                "Espinaca",
                "Perejil",
                "Piña",
                "1 naranja",
                "1 limón",
                "Miel",
                "250 ml de agua"
            ],
            "steps": [
                "Colocarlo todo en la licuadora y servirlo."
            ],
            "notes": "Categoría manuscrita: Cena."
        },
        {
            "kind": "recipe",
            "title": "Batido",
            "normalized_title": "batido",
            "is_continuation": False,
            "ingredients": [
                "1 zanahoria",
                "1 pepino",
                "1 apio",
                "2 manzanas",
                "1 limón",
                "Jengibre molido",
                "250 ml de agua"
            ],
            "steps": [
                "Colocarlo todo en la licuadora y servirlo."
            ],
            "notes": "Categoría manuscrita: Cena."
        }
    ]
}

# Page 283
pages["page_283"] = {
    "page": "283",
    "file": "recetario _283.jpg",
    "model": "gemini-3.8-flash",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "Huevos con hierbas",
            "normalized_title": "huevos con hierbas",
            "is_continuation": False,
            "ingredients": [
                "2 huevos",
                "Cebolla",
                "1/2 chile pimiento rojo",
                "1/2 chile pimiento verde",
                "1 zucchini",
                "Especias",
                "Pimienta blanca",
                "Perejil",
                "Orégano",
                "Albahaca",
                "Sal de hierbas"
            ],
            "steps": [
                "Saltear la cebolla, pimientos y zucchini con las hierbas y especias.",
                "Batir los huevos con sal de hierbas y pimienta, incorporar a las verduras y cocinar hasta que cuaje."
            ],
            "notes": "Categoría manuscrita: Cena."
        }
    ]
}

# Page 284
pages["page_284"] = {
    "page": "284",
    "file": "recetario _284.jpg",
    "model": "gemini-3.8-flash",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "Ensalada Murciana",
            "normalized_title": "ensalada murciana",
            "is_continuation": False,
            "ingredients": [
                "2 papas pequeñas",
                "3 tomates pequeños",
                "1 cebolla",
                "2 huevos duros",
                "Olivas negras",
                "1 lata de atún (opcional)",
                "Aliño:",
                "Sal de hierbas",
                "Aceite de oliva",
                "Vinagre de manzana"
            ],
            "steps": [
                "Cocer las papas y los huevos duros; cortar en cubos junto con los tomates y cebolla.",
                "Mezclar con las olivas negras y el atún si se desea.",
                "Bañar con el aliño de sal de hierbas, aceite de oliva y vinagre de manzana."
            ],
            "notes": ""
        }
    ]
}

# Page 285
pages["page_285"] = {
    "page": "285",
    "file": "recetario _285.jpg",
    "model": "gemini-3.8-flash",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "Arroz Cocido",
            "normalized_title": "arroz cocido",
            "is_continuation": False,
            "ingredients": [
                "Arroz corriente",
                "Tomate",
                "2 miltomates",
                "Chile pimiento",
                "Cebolla",
                "Clavo",
                "Pimienta",
                "Zanahoria",
                "Papa"
            ],
            "steps": [
                "Sofreír el arroz con cebolla, tomate, miltomates y chile pimiento.",
                "Agregar agua, clavo, pimienta, zanahoria y papa cortadas en cubitos.",
                "Cocinar tapado a fuego bajo hasta que el grano esté cocido y el líquido se consuma."
            ],
            "notes": ""
        }
    ]
}

# Page 286
pages["page_286"] = {
    "page": "286",
    "file": "recetario _286.jpg",
    "model": "gemini-3.8-flash",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "Pavo",
            "normalized_title": "pavo",
            "is_continuation": False,
            "ingredients": [
                "Pavo",
                "Sal, mostaza y pimienta",
                "2 tazas de vino blanco",
                "2 tazas de Coca-Cola",
                "2 tazas de cerveza",
                "Salsa para el pavo:",
                "6 ajos",
                "Tomillo",
                "Laurel",
                "Pimienta molida",
                "Nuez moscada",
                "Clavo",
                "Jengibre",
                "Chile guajillo",
                "Cebolla y tomate",
                "Sal",
                "Ketchup",
                "Piña, manzana, pasas"
            ],
            "steps": [
                "Sal, mostaza y pimienta se dejan en salmuera con el pavo.",
                "Se le aplican 2 tazas de vino blanco, 2 tazas de Coca-Cola y 2 tazas de cerveza.",
                "Para la salsa: licuar ajos, tomillo, laurel, pimienta molida, nuez moscada, clavo, jengibre, chile guajillo, cebolla, tomate, sal y ketchup.",
                "Agregar a la salsa piña, manzana y pasas.",
                "Bañar el pavo con la salsa y hornear."
            ],
            "notes": ""
        }
    ]
}

# Page 287
pages["page_287"] = {
    "page": "287",
    "file": "recetario _287.jpg",
    "model": "gemini-3.8-flash",
    "skip_reason": "",
    "items": [
        {
            "kind": "recipe",
            "title": "Enchiladas Suizas",
            "normalized_title": "enchiladas suizas",
            "is_continuation": False,
            "ingredients": [
                "6 a 8 miltomates",
                "4 tomates verdes",
                "1 cebolla",
                "1 diente de ajo",
                "2 cucharadas de crema agria",
                "Queso Oaxaca o mozzarella",
                "1 cucharada de cilantro picado",
                "Tortillas de maíz y pollo (relleno)"
            ],
            "steps": [
                "Cocer los miltomates y tomates verdes con cebolla y ajo.",
                "Licuar con la crema agria y el cilantro picado.",
                "Rellenar las tortillas con pollo, bañar con la salsa verde suiza y cubrir con queso Oaxaca o mozzarella.",
                "Gratinar en el horno hasta dorar el queso."
            ],
            "notes": ""
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

print(f"Batch 30 ({len(pages)} pages) generated successfully.")
