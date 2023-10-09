from prettytable import PrettyTable
data_user = { "Username " : "Gintoki","Password" :"Gintama"}
# List data item (game ps 2)
data_item = [
    ["1", "007: Agent Under Fire", 2000],
    ["2", "007: From Russia With Love Mirror", 2000],
    ["3", "And 1 Streetball", 2000],
    ["4", "Army Men: Air Attack ", 2000],
    ["5", "Army Men: Sarge's Heroes ", 2000],
    ["6", "Avatar: The Last Airbender", 2000],
    ["7", "Avatar The Last Airbender: Burning Earth", 2000],
    ["8", "Avatar The Last Airbender: Into the Inferno", 2000],
    ["9", "Bad Boys: Miami Takedown", 2000],
    ["10", "Band Hero", 2000],
    ["11", "Batman Begins", 2000],
    ["12", "Bakugan Battle Brawlers", 2000],
    ["13", "Battlefield 2: Modern Combat", 2000],
    ["14", "Bee Movie Game", 2000],
    ["15", "Ben 10: Alien Force Vilgax Attack Mirrors", 2000],
    ["16", "Ben 10 - Protector of Earth", 2000],
    ["17", "Ben 10 Ultimate Alien: Cosmic Destruction", 2000],
    ["18", "Blade 2", 2000],
    ["19", "Black", 2000],
    ["20", "Bloody Roar 3", 2000],
    ["21", "Bloody Roar 4", 2000],
    ["22", "BMX XXX", 2000],
    ["23", "Bolt", 2000],
    ["24", "Brothers In Arms: Earned In Blood", 2000],
    ["25", "Brothers in Arms: Road to Hill 30", 2000],
    ["26", "Burnout", 2000],
    ["27", "Burnout 2: Point of Impact", 2000],
    ["28", "Burnout 3 - Takedown", 2000],
    ["29", "Burnout Dominator", 2000],
    ["30", "Burnout Revenge", 2000],
    ["31", "Call of Duty: Finest Hour", 2000],
    ["32", "Call of Duty 2: Big Red One", 2000],
    ["33", "Call of Duty 3", 2000],
    ["34", "Call of Duty: World At War Final Fronts", 2000],
    ["35", "Capcom Fighting Evolution", 2000],
    ["36", "Capcom vs. SNK 2: Mark of the Millennium 2001", 2000],
    ["37", "Cars", 2000],
    ["38", "Cars Race-O-Rama", 2000],
    ["39", "Cartoon Network Racing", 2000],
    ["40", "Casper: Spirit Dimensions", 2000],
    ["41", "Castlevania: Curse of Darkness", 2000],
    ["42", "Castlevania: Lament of Innocence", 2000],
    ["43", "Catwoman", 2000],
    ["44", "Chronicles of Narnia: The Lion, The Witch and The Wardrobe", 2000],
    ["45", "Chronicles of Narnia: Prince Caspian", 2000],
    ["46", "Conflict: Global Terror", 2000],
    ["47", "Conflict: Vietnam", 2000],
    ["48", "Contra: Shattered Soldier", 2000],
    ["49", "Constantine", 2000],
    ["50", "Crash of the Titans", 2000],
    ["51", "Crash Tag Team Racing", 2000],
    ["52", "Dance Dance Revolution - Max", 2000],
    ["53", "Dance Dance Revolution - Max 2", 2000],
    ["54", "Dance Dance Revolution X", 2000],
    ["55", "Dance Dance Revolution X2", 2000],
    ["56", "Dead or Alive 2: Hardcore", 2000],
    ["57", "Def Jam: Fight for NY", 2000],
    ["58", "Def Jam: Vendetta", 2000],
    ["59", "Despicable Me", 2000],
    ["60", "Devil May Cry", 2000],
    ["61", "Devil May Cry 2", 2000],
    ["62", "Devil May Cry 3: Dante's Awakening", 2000],
    ["63", "Digimon Rumble Arena 2", 2000],
    ["64", "Disney Princess: Enchanted Journey", 2000],
    ["65", "Disney's Chicken Little", 2000],
    ["66", "Disney's Tarzan Untamed", 2000],
    ["67", "Downhill Domination", 2000],
    ["68", "Dragon Ball Z: Budokai", 2000],
    ["69", "Dragon Ball Z: Budokai 2", 2000],
    ["70", "Dragon Ball Z: Budokai 3", 2000],
    ["71", "Dragon Ball Z: Budokai Tenkaichi 3", 2000],
    ["72", "Dragon Ball Z Sagas", 2000],
    ["73", "Dynasty Warriors 2", 2000],
    ["74", "Dynasty Warriors 3", 2000],
    ["75", "Dynasty Warriors 4", 2000],
    ["76", "Dynasty Warriors 6", 2000],
    ["77", "Enter the Matrix", 2000],
    ["78", "ESPN College Hoops", 2000],
    ["79", "ESPN College Hoops 2k5", 2000],
    ["80", "Evil Dead: A Fistful of Boomstick", 2000],
    ["81", "Evil Dead: Regeneration", 2000],
    ["82", "Fairly OddParents: Breakin' Da Rules", 2000],
    ["83", "Fallout: Brotherhood of Steel", 2000],
    ["84", "Family Guy", 2000],
    ["85", "Fantastic 4", 2000],
    ["86", "Fast and the Furious", 2000],
    ["87", "FIFA Soccer 11", 2000],
    ["88", "FIFA Street", 2000],
    ["89", "FIFA Street 2", 2000],
    ["90", "Final Fantasy VII: Dirge of Cerberus", 2000],
    ["91", "Final Fantasy X", 2000],
    ["92", "Final Fantasy XI", 2000],
    ["93", "Final Fantasy XII", 2000],
    ["94", "Finding Nemo", 2000],
    ["95", "Fisherman's Bass Club", 2000],
    ["96", "Fullmetal Alchemist and the Broken Angel", 2000],
    ["97", "Fullmetal Alchemist 2: Curse of the Crimson Elixir", 2000],
    ["98", "Genji - Dawn of the Samurai", 2000],
    ["99", "George of the Jungle", 2000],
    ["100", "Ghostbusters - The Video Game", 2000],
    ["101", "Ghost Rider", 2000],
    ["102", "G.I. Joe: The Rise of Cobra", 2000],
    ["103", "Godfather", 2000],
    ["104", "God Hand", 2000],
    ["105", "God of War", 2000],
    ["106", "God of War II", 2000],
    ["107", "Godzilla Unleashed", 2000],
    ["108", "Grand Prix Challenge", 2000],
    ["109", "Grand Theft Auto III", 2000],
    ["110", "Grand Theft Auto: Liberty City Stories", 2000],
    ["111", "Grand Theft Auto: San Andreas", 2000],
    ["112", "Grand Theft Auto: Vice City", 2000],
    ["113", "Grand Theft Auto: Vice City Stories", 2000],
    ["114", "Gran Turismo 3: A-Spec", 2000],
    ["115", "Gran Turismo 4", 2000],
    ["116", "Guilty Gear X", 2000],
    ["117", "Guilty Gear X2", 2000],
    ["118", "Guitar Hero", 2000],
    ["119", "Guitar Hero III - Legends of Rock", 2000],
    ["120", "Guitar Hero 5", 2000],
    ["121", "Guitar Hero - World Tour", 2000],
    ["122", "Half-Life", 2000],
    ["123", "Harry Potter and The Chamber of Secrets", 2000],
    ["124", "Harry Potter and The Goblet of Fire", 2000],
    ["125", "Harry Potter and The Half-Blood Prince", 2000],
    ["126", "Harry Potter and The Order of the Phoenix", 2000],
    ["127", "Harry Potter and The Prisoner of Azkaban", 2000],
    ["128", "Harry Potter and The Sorcerers Stone", 2000],
    ["129", "Harvest Moon: A Wonderful Life", 2000],
    ["130", "Harvest Moon: Save The Homeland", 2000],
    ["131", "Haunted Mansion", 2000],
    ["132", "Hitman: Blood Money", 2000],
    ["133", "Hitman: Contracts", 2000],
    ["134", "Hitman 2: Silent Assassin", 2000],
    ["135", "Hot Wheels: Beat That", 2000],
    ["136", "Hot Wheels World Race", 2000],
    ["137", "Hulk", 2000],
    ["138", "Ice Age: Dawn of the Dinosaurs", 2000],
    ["139", "Ice Age 2: The Meltdown", 2000],
    ["140", "Incredible Hulk, The: Ultimate Destruction", 2000],
    ["141", "Incredibles: Rise of the Underminer", 2000],
    ["142", "Indiana Jones and the Emperor’s Tomb", 2000],
    ["143", "InuYasha: Feudal Combat", 2000],
    ["144", "Iron Man", 2000],
    ["145", "James Bond 007: Agent Under Fire", 2000],
    ["146", "James Bond 007: Everything or Nothing", 2000],
    ["147", "James Bond 007: NightFire", 2000],
    ["148", "Jimmy Neutron Boy Genius", 2000],
    ["149", "Just Cause", 2000],
    ["150", "King Kong", 2000],
    ["151", "Kingdom Hearts", 2000],
    ["152", "Kingdom Hearts 2", 2000],
    ["153", "Kingdom Hearts Re:Chain of Memories", 2000],
    ["154", "King of Fighters: Maximum Impact", 2000],
    ["155", "King of Fighters Collection, The: The Orochi Saga", 2000],
    ["156", "Lego Batman - The Video Game", 2000],
    ["157", "Lego Indiana Jones - The Original Adventures", 2000],
    ["158", "Lego Star Wars - The Video Game", 2000],
    ["159", "Lego Star Wars II - The Original Trilogy", 2000],
    ["160", "Madagascar", 2000],
    ["161", "Madden NFL 11", 2000],
    ["162", "Mafia", 2000],
    ["163", "Major League Baseball 2K6", 2000],
    ["164", "Manhunt", 2000],
    ["165", "Manhunt 2", 2000],
    ["166", "Marvel Nemesis - Rise of the Imperfects", 2000],
    ["167", "Marvel vs Capcom 2 - New Age of Heroes", 2000],
    ["168", "Marvel Ultimate Alliance", 2000],
    ["169", "Marvel Ultimate Alliance 2", 2000],
    ["170", "Max Payne", 2000],
    ["171", "Max Payne 2: The Fall of Max Payne", 2000],
    ["172", "Medal of Honor: European Assault", 2000],
    ["173", "Medal of Honor: Frontline", 2000],
    ["174", "Medal of Honor: Rising Sun", 2000],
    ["175", "Medal of Honor: Vanguard", 2000],
    ["176", "Mega Man X8", 2000],
    ["177", "Metal Gear Solid 3 - Snake Eater", 2000],
    ["178", "Metal Gear Solid 3 - Subsistence - Limited Edition", 2000],
    ["179", "Metal Slug 4 & 5", 2000],
    ["180", "Midnight Club Street Racing", 2000],
    ["181", "Mobile Suit Gundam: Zeonic Front", 2000],
    ["182", "Monster Jam", 2000],
    ["183", "Mortal Kombat - Armageddon", 2000],
    ["184", "Mortal Kombat - Deadly Alliance", 2000],
    ["185", "Mortal Kombat - Deception", 2000],
    ["186", "Mortal Kombat - Shaolin Monks", 2000],
    ["187", "MotoGP 07", 2000],
    ["188", "Musashi: Samurai Legend", 2000],
    ["189", "Naruto Ultimate Ninja", 2000],
    ["190", "Naruto - Ultimate Ninja 2", 2000],
    ["191", "Naruto - Ultimate Ninja 3", 2000],
    ["192", "Naruto Uzumaki Chronicles", 2000],
    ["193", "Naruto: Uzumaki Chronicles 2", 2000],
    ["194", "NBA 2K3", 2000],
    ["195", "NBA Live 2004", 2000],
    ["196", "NBA Street V3", 2000],
    ["197", "Need for Speed - Carbon", 2000],
    ["198", "Need for Speed: Most Wanted", 2000],
    ["199", "Need for Speed: Underground", 2000],
    ["200", "One Piece: Pirates' Carnival", 2000],
    ["201", "Pac-Man Collection - 3-in-1", 2000],
    ["202", "Persona 4", 2000],
    ["203", "Pirates of the Caribbean: At World's End", 2000],
    ["204", "Prince of Persia: The Sands of Time", 2000],
    ["205", "Prince of Persia: The Two Thrones", 2000],
    ["206", "Pro Evolution Soccer 2009", 2000],
    ["207", "Pump It Up: Exceed", 2000],
    ["208", "Ratatouille", 2000],
    ["209", "Resident Evil 4", 2000],
    ["210", "Resident Evil Code: Veronica X", 2000],
    ["211", "Resident Evil Outbreak", 2000],
    ["212", "Resident Evil - Dead Aim", 2000],
    ["213", "Rumble Racing", 2000],
    ["214", "Samurai Champloo: Sidetracked", 2000],
    ["215", "Samurai Warriors 2 - Xtreme Legends", 2000],
    ["216", "Scooby-Doo! Night of 100 Frights", 2000],
    ["217", "Shadow of the Colossus", 2000],
    ["218", "Silent Hill Origins", 2000],
    ["219", "Silent Hill: Shattered Memories", 2000],
    ["220", "Spider-Man - Web of Shadows", 2000],
    ["221", "SpongeBob: Globs of Doom", 2000],
    ["222", "Superman Returns", 2000],
    ["223", "Teenage Mutant Ninja Turtles", 2000],
    ["224", "Teen Titans", 2000],
    ["225", "Tekken 4", 2000],
    ["226", "Tekken 5", 2000],
    ["227", "Tekken Tag Tournament", 2000],
    ["228", "Terminator 3: Rise of the Machines", 2000],
    ["229", "The Warriors", 2000],
    ["230", "Tomb Raider: Legend", 2000],
    ["231", "Tom Clancy's Ghost Recon", 2000],
    ["232", "Tom Clancy's Rainbow Six: Lockdown", 2000],
    ["233", "Tom Clancy's Splinter Cell", 2000],
    ["234", "Tony Hawk's Pro Skater 4", 2000],
    ["235", "Tony Hawk’s Underground", 2000],
    ["236", "Transformers: The Game", 2000],
    ["237", "Transformers: Revenge of the Fallen", 2000],
    ["238", "Twisted Metal: Head On - Extra Twisted Edition", 2000],
    ["239", "Ultimate Spider-Man", 2000],
    ["240", "Up", 2000],
    ["241", "Van Helsing", 2000],
    ["242", "Virtua Fighter 4: Evolution", 2000],
    ["243", "Wall-E", 2000],
    ["244", "Warhammer 40,000: Fire Warrior", 2000],
    ["245", "Way of The Samurai 2", 2000],
    ["246", "WWE All Stars", 2000],
    ["247", "WWE SmackDown! vs Raw 2011", 2000],
    ["248", "X-Men - Origins - Wolverine", 2000],
    ["249", "Yakuza", 2000],
    ["250", "Yakuza 2", 2000],
    ["251", "Yu-Gi-Oh! The Duelists of the Roses", 2000],
    ["252", "Yu Yu Hakusho - Dark Tournament", 2000],
    ["253", "Zathura", 2000],
] 

    

# pembeli
def transaksi():
    while True:
        # Menampilkan seluruh Game yang ada
        print("Daftar Game yang ready")
        show_item()
        
        # input nomor kode game 
        kode_game = input("Masukkan kode game yang ingin dibeli: ")
        quantity = int(input("Masukkan jumlah kaset yang ingin dibeli: "))
        
        # Memeriksa jumlah kaset yang ingin dibeli (hanya boleh 1)
        for item in data_item:
            if item[0] == kode_game:
                if quantity > 1:
                    print("Maaf, jumlah maksimum pembelian kaset hanya 1 !")
                    break
        else:
            # menampilkan total harga
            for i in range(len(data_item)):
                if data_item[i][0] == kode_game:
                    total_harga = data_item[i][2] * quantity
                    print("Total harga: Rp", total_harga),
                    print("+"*41)
                    print("++                                     ++")
                    print("++  TERIMA KASIH SUDAH MEMBELI DISINI  ++")
                    print("++                                     ++")
                    print("+"*41)
                    print(" ")
                    
                    return
              
        
        # Menampilkan ulang daftar game apabila  jumlah yang diinput salah(lebih dari 1)
        print()

# admin
def create():
    # Input data game yang baru
    kode_game = input("Masukkan nomor kode game: ")
    nama_game = input("Masukkan nama game: ")
    harga_kaset = int(input("Masukkan harga kaset: "))
    
    # Menambahkan game yang baru ke dalam database
    data_item.append([kode_game, nama_game, harga_kaset])
    
    # Menampilkan daftar game lengkap dengan game baru yang ditambahkan
    show_item()

def read():
    # Menampilkan seluruh game yang terdapat dalam database
    show_item()

def update():
    # Input nomor kode game yang ingin diperbarui
    kode_game = input("Masukkan kode game yang ingin di-update data: ")
    for i in range(len(data_item)):
        if data_item[i][0] == kode_game:
            
            # Input data game yang baru
            nama_game = input("Masukkan nama game baru: ")
            harga_game = int(input("Masukkan harga game baru: "))
            
            # melakukan update item yang dipilih
            data_item[i][1] = nama_game
            data_item[i][2] = harga_game
            
            # menampilkan daftar item yang terbaru
            show_item()
            break
    else:
        print("Game tidak ada")

def delete():
    # input nomor game yang ingin dihapus
    nomor_game = input("Masukkan nomor game yang ingin dihapus: ")
    for i in range(len(data_item)):
        if data_item[i][0] == nomor_game:
            
            # Menghapus game sesuai input nomor
            data_item.pop(i)
            
            # Menampilkan daftar game terbaru
            show_item()
            break
    else:
        print("Game tidak ada")
    
# menampilkan seluruh item yang terdapat dalam database dengan prettytable
def show_item():
    table = PrettyTable()
    table.field_names = ["Nomor", "Nama Game", "Harga/Kaset"]
    for item in data_item:
        table.add_row(item)
    print(table)

# Main Program
while True :
    print("+"*41)
    print("++                                     ++")
    print("++ SELAMAT DATANG DI PLAYSTATION MANIA ++")
    print("++                                     ++")
    print("+"*41)
    print(" ")
    # Input Pengguna (1/2/3)
    print ("1. Admin (login) ")
    print ("2. Pembeli ")
    print ("3. Keluar ")
    print(" ")
    status = input("Siapa anda??? : ")

# Jika masuk sbg Admin
    if status == "1":
        # jumlah percobaan login
        # jumlah percobaan login
        max_attempts = 3
        attempts = 0
        logged_in = False
        while attempts < max_attempts:
            user = input("Masukkan username anda : ")
            pw = input("Masukkan password anda : ")
            if user == data_user["Username "] and pw == data_user["Password"]:
                print("Selamat anda telah masuk!!!")
                logged_in = True
                break
            else:
                print("Username atau password yang dimasukkan salah!")
                attempts += 1
                if attempts < max_attempts:
                    print(f"Kamu punya {max_attempts - attempts} kesempatan untuk mencoba lagi")
                else:
                    print("Percobaan habis. Kembali")
                    break
        if not logged_in:  
            continue

        while True:
            print("+"*40)
            print("Admin Playstation Mania")
            print("+"*40)
            print("1. Tambah Game")
            print("2. Lihat Game")
            print("3. Update Game")
            print("4. Hapus Game")
            print("5. Kembali")

            admin_choice = input("Pilih menu: ")
            if admin_choice == "1" :
                create()
            elif admin_choice == "2":
                read()
            elif admin_choice == "3":
                update()
            elif admin_choice == "4":
                delete()
            elif admin_choice == "5":
                break  # Exit the admin menu loop and go back to the main menu
            else:
                print("Menu tidak tersedia")
    #Jika Masuk sbg pembeli
    elif status == "2":
        print("="*30)
        print("PEMBELI")
        print("="*30)
        transaksi()
    elif status == "3":
        print("Terima kasih telah mengunjungi Playstation Mania!!!")
        break
    else:
        print("Menu tidak tersedia")

