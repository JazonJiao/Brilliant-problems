def find(A):
    arr = [0]
    arr = arr * 8
    for i in A:
        if i[1] < 'D':
            arr[i[2]] += 1
        
    return arr

A = [("Barney Belfield", 'L', 4),("Ricky Robinson", 'Q', 7),("Keren Knisely", 'W', 7),("Usha Umphrey", 'X', 1),("Seema Sandler", 'Y', 2),("Tereasa Torres", 'R', 7),("Siu Savage", 'L', 3),("Harrison Hunley", 'F', 7),("Margarett Millhouse", 'W', 2),("Lue Leftwich", 'X', 4),("Stuart Schimmel", 'J', 6),("Trenton Throneberry", 'I', 7),("Amira Amaker", 'Q', 4),("Tia Thistle", 'S', 6),("Loreta Lease", 'B', 5),("Mika Magyar", 'K', 1),("Reiko Riddles", 'W', 4),("Osvaldo Osteen", 'U', 1),("Toney Thatch", 'K', 7),("Arden Arch", 'F', 2),("Terrence Thornton", 'A', 5),("Evonne Edlund", 'R', 1),("Darcey Delariva", 'D', 1),("Drew Dessert", 'I', 7),("Chun Cheshire", 'E', 2),("Grayce Guyton", 'O', 5),("Aracelis Archambault", 'B', 3),("Collen Cousar", 'K', 1),("Stacie Sauders", 'I', 7),("Merrill Marksberry", 'S', 6),("Alina Anastasio", 'Q', 6),("Robbin Roles", 'D', 4),("Venice Valiente", 'K', 7),("Klara Koehn", 'U', 6),("Maragret Maxwell", 'O', 2),("Tina Tyrrell", 'O', 3),("Naomi Najera", 'W', 3),("Sook Stidham", 'E', 7),("Eula Esperanza", 'X', 5),("Verlie Veres", 'P', 4),("Sigrid Spanos", 'J', 1),("Lenny Leverett", 'W', 2),("Nola Necaise", 'P', 7),("Jerri Jess", 'Y', 1),("Phyllis Pullin", 'E', 7),("Carie Collins", 'I', 4),("Luvenia Lamer", 'J', 5),("Luigi Lucio", 'N', 3),("Carletta Crowden", 'P', 2),("Blaine Bombard", 'H', 3),("Alton April", 'W', 7),("Hortensia Hammer", 'K', 4),("Wynona Wagener", 'I', 3),("Myra Moritz", 'S', 2),("Mira Mask", 'Q', 1),("Hollis Hamner", 'B', 4),("Helena Howey", 'X', 7),("Daron Denker", 'A', 3),("Araceli Apel", 'W', 3),("Raelene Rimer", 'S', 5),("Regena Rhoda", 'V', 1),("Setsuko Spell", 'N', 3),("Scott Stagg", 'H', 4),("Chassidy Cullen", 'M', 5),("Mozell Motton", 'U', 2),("Trey Tavera", 'L', 6),("Teena Tabares", 'V', 1),("Bessie Brook", 'L', 4),("Rusty Rosenblatt", 'M', 1),("Camille Collins", 'R', 5),("Zenia Zurita", 'L', 2),("Eli Euell", 'Z', 4),("Lillia Lack", 'K', 2),("My Metayer", 'R', 1),("Rubi Rorie", 'U', 3),("Rhea Rutt", 'K', 2),("Mickie Midgette", 'W', 5),("Hosea Hust", 'R', 2),("Hannah Horrocks", 'G', 4),("Armanda Allinder", 'D', 3),("Denis Downard", 'N', 2),("Adelaida Ashbaugh", 'Y', 3),("Giovanna Grimmer", 'Y', 2),("Risa Rucks", 'E', 6),("Rosanne Rudolph", 'C', 6),("Carolina Claar", 'S', 5),("Katherine Kiefer", 'B', 5),("Caroline Cruise", 'B', 3),("Yoshie Yager", 'V', 3),("Princess Pinon", 'X', 6),("Antony Anding", 'B', 5),("Rachell Rollins", 'B', 2),("Krystin Kehl", 'G', 4),("Rowena Roan", 'W', 5),("Kristofer Killeen", 'J', 1),("Lai Labrie", 'M', 5),("Corazon Chiarello", 'O', 3),("Margareta Magnusson", 'J', 5),("Agueda Almond", 'J', 7),("Victor Varney", 'Z', 5),("Jamika Johannsen", 'M', 6),("Clarence Collyer", 'O', 7),("Allyn Alva", 'G', 4),("Ervin Elizondo", 'D', 6),("Alexandria Alper", 'I', 2),("Lara Labrie", 'Q', 7),("Flor Faunce", 'A', 2),("Lonnie Laforge", 'S', 3),("Shandra Samples", 'Q', 2),("Nicolas Neugebauer", 'X', 4),("Ivana Isaac", 'L', 3),("Ellamae Eutsler", 'T', 7),("Celestina Counter", 'Q', 5),("Theron Tekulve", 'Z', 1),("Sabra Sund", 'X', 3),("Jeffery Jilek", 'S', 6),("Kati Krings", 'E', 2),("Dakota Degraw", 'K', 4),("Virginia Vogl", 'H', 5),("Delaine Dorsch", 'X', 5),("Vernie Valley", 'L', 4),("Clelia Churchill", 'F', 4),("Georgiana Guercio", 'K', 3),("Maricela Mehl", 'D', 1),("Shana Sarinana", 'O', 4),("Jonelle Jacques", 'S', 7),("Daniell Dicus", 'J', 1),("Bernita Birchfield", 'K', 1),("Deane Dinardo", 'I', 5),("Merle Mccorkle", 'J', 6),("Berneice Borchers", 'K', 5),("Kendra Keil", 'V', 1),("Buddy Busby", 'W', 7),("Valerie Valdes", 'E', 6),("Harriett Hodel", 'K', 7),("Onita Oberholtzer", 'L', 3),("Zofia Zachery", 'Y', 1),("Arlyne Axel", 'S', 3),("Adelaida Alaimo", 'W', 7),("Theola Tash", 'Q', 4),("Latashia Leary", 'R', 7),("Floretta Fehrenbach", 'L', 4),("Lovetta Lapointe", 'K', 3),("Brenda Bollinger", 'N', 1),("Margit Mullett", 'Y', 7),("Melita Mater", 'S', 3),("Lori List", 'J', 5),("Chase Corriveau", 'U', 5),("Marni Moots", 'P', 6),("Gaye Gumm", 'J', 2),("Victor Vanfossen", 'Z', 2),("Harold Heidecker", 'A', 7),("Agnus Alsop", 'L', 4),("Lien Leverich", 'E', 3),("Devona Day", 'N', 2),("Ladawn Lalli", 'D', 5),("Berta Bader", 'U', 7),("Joni Joynt", 'V', 2),("Floria Fedrick", 'U', 3),("Jerald Jo", 'Z', 1),("Kimberly Kraft", 'B', 2),("Juliane Jablonowski", 'Z', 7),("Marisela Matchett", 'Z', 6),("Terry Turney", 'B', 7),("Alissa Amsden", 'S', 3),("Lecia Lassiter", 'T', 6),("Ozella Orzechowski", 'L', 4),("Nena Nitta", 'Q', 2),("Young Youngren", 'X', 6),("Renda Raso", 'B', 7),("Barabara Bargo", 'S', 1),("Afton Alldredge", 'F', 3),("Alessandra Abreu", 'X', 1),("Jacquelin Job", 'L', 7),("Clarence Cuenca", 'L', 5),("Billye Band", 'P', 2),("Kimiko Kornfeld", 'K', 5),("Lynne Lapeyrouse", 'J', 3),("Marguerita Molder", 'X', 5),("Karole Kepner", 'G', 6),("Drusilla Dollison", 'O', 2),("Adrian Antunez", 'X', 7),("Rosita Reinke", 'A', 5),("Belia Beltrami", 'Y', 1),("Janina Jay", 'Y', 1),("Gregg Grieves", 'N', 6),("Darwin Durr", 'T', 1),("Lucie Lundberg", 'D', 5),("Vergie Vetrano", 'G', 3),("Francene Francese", 'M', 1),("Barbie Baily", 'E', 6),("Lyndsay Landman", 'V', 3),("Elma Emerson", 'G', 5),("Eugena Eppinger", 'O', 4),("Xiao Xie", 'W', 1),("Latashia Leech", 'W', 4),("Eboni Eastin", 'E', 5),("Zenaida Zink", 'J', 7),("Rachell Rasmusson", 'Y', 5),("Althea Almaguer", 'S', 3)]

print(find(A))