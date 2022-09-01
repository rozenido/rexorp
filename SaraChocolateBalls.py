import random
from tkinter import *
from tkinter.font import Font
import webbrowser
# Window Settings and Fonts:#################
window = Tk()
window.geometry("1000x800")
window.title("Sara's chocolate balls")
window.columnconfigure(4)
frame = Frame(window)
leftframe = Frame(window)
leftframe.pack(side=LEFT)
rightframe = Frame(window)
rightframe.pack(side=RIGHT)
Window_scroll_Y = Scrollbar(window)
Window_scroll_Y.pack(side=RIGHT, fill=Y)
TitleFont = Font(family="Helvetica", size=42, underline=1)
colors = ['red', 'blue', 'yellow', 'green', '#ffb3fe', 'pink', 'grey']
result_lable = Label(window, text="Best results:", font='Aril 30 underline')

# Main  Title:############################
MainLabel = Label(window, text="Sara's search engine", font='Helvetica 42 underline')
MainLabel.place(rely=0.08, relx=0.26)

# Main Entry box and search button#########################
e = Entry(window, width=40, borderwidth=3, font='Arial 20')
e.place(rely=0.2, relx=0.24)
# List datas by catagory:
cookies = ["cookies", "flour", "Flour", "cookie", "Cookie", "Cookies", "butter", "chocolate", "baking", "powder"]
Vegetables = ["spinach", "carrot", "carrots", "broccoli", "garlic", "tomato", "onion", "lettuce", "cucumber", "vegetable", "salad"]
Fruits = " "
Grains = " "
Protein_Foods = " "
Dairy = " "
oils_Solid_Fats = " "
Added_Sugars = " "
Beverages = " "


# Food windows functions:
def chocolate_ball_window():
    chocolate_ball_screen = Toplevel()
    chocolate_ball_screen.title("Chocolate ball recipe")
    chocolate_ball_screen.geometry("600x400")
    r1 = Listbox(chocolate_ball_screen, font= 'Arial 20', width=50)
    r1.insert(1, "Ingredients:")
    r1.insert(2, "200-250 grams cookies (preferably Petit Beurre)")
    r1.insert(3, "2 fluid ounces sugar")
    r1.insert(4, "4.5 tbsp unsweetened cocoa")
    r1.insert(5, "4 oz unsalted butter (melted)")
    r1.insert(6, "1 tsp vanilla extract")
    r1.insert(7, "4-5 tbsp milk")
    r1.insert(8, "Coconut sprinkles for dipping (or anything else you so desire)")
    chocolate_ball = Label(chocolate_ball_screen, text="Chocolate Balls:", font='Aril 22')
    r1.pack()
    chocolate_ball.place(in_=r1,rely=-0.15)
def basic_cookie_window():
    basic_cookie_screen = Toplevel()
    basic_cookie_screen.title("Basic cookie recipe")
    basic_cookie_screen.geometry("800x600")
    r2 = Listbox(basic_cookie_screen, font='Arial 20', width=100, height=100)
    r2.insert(1,"225g butter, softened")
    r2.insert(2,"110g caster sugar")
    r2.insert(3,"275g plain flour")
    r2.insert(4,"1 tsp cinnamon or other spices (optional)")
    r2.insert(5,"75g white or milk chocolate chips (optional)")
    r2.insert(6,"         how to make:                       ")
    r2.insert(7,"Heat the oven to 190C/170C fan/gas 5.")
    r2.insert(8," Cream the butter in a large bowl with a wooden spoon or in a stand mixer until it is soft.")
    r2.insert(9," Add the sugar and keep beating until the mixture is light and fluffy.")
    r2.insert(10," Sift in the flour and add the optional ingredients, if you’re using them.")
    r2.insert(11," Bring the mixture together with your hands in a figure-of-eight motion until it forms a dough.")
    r2.insert(12," You can freeze the dough at this point.")
    r2.pack()
    basic_cookie = Label(basic_cookie_screen, text="Basic cookie:", font='Aril 22')
    basic_cookie.place(in_=r2, rely=-0.15)
def vintage_chocolate_chip_window():
    vintage_chocolate_chip_screen = Toplevel()
    vintage_chocolate_chip_screen.title("Vintage chocolate chip cookies")
    vintage_chocolate_chip_screen.geometry("800x600")
    d1 = Listbox(vintage_chocolate_chip_screen, font='Arial 20', width=100, height=100)
    d1.insert(1,"150g salted butter, softened")
    d1.insert(2,"80g light brown muscovado sugar")
    d1.insert(3,"80g granulated sugar")
    d1.insert(4,"2 tsp vanilla extract")
    d1.insert(5,"1 large egg")
    d1.insert(6,"225g plain flour")
    d1.insert(7,"half tsp bicarbonate of soda")
    d1.insert(8,"1/4 tsp salt")
    d1.insert(9,"200g plain chocolate chips or chunks")
    d1.insert(10,"                    how to make:")
    d1.insert(11,"Heat the oven to 190C/fan170C/gas 5 and line two baking sheets with non-stick baking paper.")
    d1.insert(12,"Put 150g softened salted butter,")
    d1.insert(13,"80g light brown muscovado sugar and 80g granulated sugar into a bowl and beat until creamy.")
    d1.insert(14,"Beat in 2 tsp vanilla extract and 1 large egg.")
    d1.insert(15,"Sift 225g plain flour,")
    d1.insert(16,"1/2 tsp bicarbonate of soda and 1/4 tsp salt into the bowl and mix it in with a wooden spoon.")
    d1.insert(17,"Add 200g plain chocolate chips or chunks and stir well.")
    d1.insert(18,"Use a teaspoon to make small scoops of the mixture, spacing them well apart on the baking trays.")
    d1.insert(19,"This mixture should make about 30 cookies.")
    d1.pack()
def double_choc_peanut_butter_window():
    double_choc_peanut_butter_screen = Toplevel()
    double_choc_peanut_butter_screen.title("Double choc peanut butter cookies")
    double_choc_peanut_butter_screen.geometry("800x600")
    f1 = Listbox(double_choc_peanut_butter_screen, font='Arial 20', width=100, height=100)
    f1.insert(1,"         Ingredients:")
    f1.insert(2,"100g unsalted butter , softened at room temperature")
    f1.insert(3,"100g light brown sugar")
    f1.insert(4,"100g caster sugar")
    f1.insert(5,"1 egg , beaten")
    f1.insert(6,"150g self-raising flour")
    f1.insert(7,"2 tbsp cocoa powder")
    f1.insert(8,"1/4 tsp salt")
    f1.insert(9,"200g milk chocolate , 150g chopped into chunks and 50g melted for drizzling")
    f1.insert(10,"75g peanut butter (crunchy or smooth is fine)")
    f1.insert(11,"handful of salted peanuts , roughly chopped")
    f1.insert(12,"milk to serve, optional")
    f1.insert(13, "                                        how to make:")
    f1.insert(14,"Heat the oven to 180c/160 fan/gas mark 4 and line two baking trays with parchment.")
    f1.insert(15," Using a food mixer or electric whisk beat the butter and sugar together until light and fluffy.")
    f1.insert(16," Add in the egg and whisk to combine then beat in the flour, cocoa powder,")
    f1.insert(17," salt and chocolate chunks until fully incorporated.")
    f1.insert(18," Using a spoon swirl the peanut butter through the cookie dough.")
    f1.insert(19,"                                           Step 2:")
    f1.insert(20,"Scoop the dough into 12 large cookies onto the two trays using a dessert spoon,")
    f1.insert(21," leaving plenty of room between each cookie as they'll spread.")
    f1.insert(22," Bake in the oven for 9-10 mins until still soft and melty in the middle.")
    f1.insert(23," They will look underbaked but will harden once cool.")
    f1.insert(24," Drizzle over the melted milk chocolate and top with a few chopped peanuts and a pinch of flaky sea salt.")
    f1.insert(25," Serve with a glass of milk for dunking.")
    f1.pack()
def vegan_chocolate_chip_window():
    vintage_chocolate_chip_screen = Toplevel()
    vintage_chocolate_chip_screen.title("Vegan chocolate chip cookies")
    vintage_chocolate_chip_screen.geometry("800x600")
    h3 = Listbox(vintage_chocolate_chip_screen, font='Arial 20', width=100, height=100)
    h3.insert(1,"              Ingredients:")
    h3.insert(2,"125g cold coconut oil")
    h3.insert(3,"100g golden caster sugar")
    h3.insert(4,"150g light muscavdo sugar")
    h3.insert(5,"125ml coconut milk")
    h3.insert(6,"1 tsp vanilla extract")
    h3.insert(7,"275g plain flour")
    h3.insert(8,"1 tsp baking powder")
    h3.insert(9,"1/4 tsp bicarb")
    h3.insert(10,"200g vegan chocolate chips or vegan chocolate, chopped into small chunks")
    h3.insert(11,"                    how to make:")
    h3.insert(12,"Tip the coconut oil and sugars into a bowl and whisk until completely combined,")
    h3.insert(13," then whisk in the coconut milk and vanilla.")
    h3.insert(14," Tip the flour, baking powder,")
    h3.insert(15," bicarb and a good pinch of flaky sea salt into the mix to make a thick batter,")
    h3.insert(16," then fold through the chocolate chips.")
    h3.insert(17," Chill the batter for at least 1hr.")
    h3.insert(18," Can be made two days ahead.")
    h3.insert(19,"Heat the oven to 180C/160C fan/gas 4.")
    h3.insert(20," Line a couple of baking sheets with baking parchment,")
    h3.insert(21," then scoop or roll plum-sized balls of the dough")
    h3.insert(22," and place them on the baking sheets about 2cm apart.")
    h3.insert(23," Flatten ever so slightly and sprinkle with a bit more flaky salt if you want.")
    h3.insert(24," Cook on the middle shelf for 12-15 mins, turning the tray once,")
    h3.insert(25," until the cookies have spread and are golden but still soft in the middle.")
    h3.insert(26," Leave to cool slightly, then lift the cookies onto a cooling rack while you bake another batch.")
    h3.insert(27," Will keep in a biscuit jar for up to three days.")
    h3.pack()
def rainbow_cookies_window():
    rainbow_cookies_screen = Toplevel()
    rainbow_cookies_screen.title("Rainbow Cookies")
    rainbow_cookies_screen.geometry("800x600")
    t5 = Listbox(rainbow_cookies_screen, font='Arial 20', width=100, height=100)
    t5.insert(1, "                    Ingredients:")
    t5.insert(2, "175g softened butter")
    t5.insert(3, "50g golden caster sugar")
    t5.insert(4, "50g icing sugar")
    t5.insert(5,"2 egg yolks")
    t5.insert(6,"2 tsp vanilla extract")
    t5.insert(7,"300g plain flour")
    t5.insert(8,"zest and juice 1 orange")
    t5.insert(9,"140g icing sugar , sifted")
    t5.insert(10, "sprinkles , to decorate")
    t5.insert(11, "                         how to make:")
    t5.insert(12,"Heat oven to 200C/180C fan/gas 6.")
    t5.insert(13," Mix the butter, sugars, egg yolks and vanilla with a wooden spoon until creamy,")
    t5.insert(14," then mix in the flour in 2 batches.")
    t5.insert(16," Stir in the orange zest.")
    t5.insert(17," Roll the dough into about 22 walnut-size balls and sit on baking sheets.")
    t5.insert(18," Bake for 15 mins until golden, then leave to cool.")
    t5.insert(19,"Meanwhile, mix the icing sugar with enough orange juice to make a thick, runny icing.")
    t5.insert(20," Dip each biscuit half into the icing, then straight into the sprinkles.")
    t5.insert(21," Dry on a wire rack.")
    t5.pack()
def cookies_extra_results():
    webbrowser.open_new(r"https://www.bbcgoodfood.com/recipes/collection/cookie-recipes?page=3")









# Result Buttons

chocolate_ball_button = Button(window, text="Chocolate balls", font='Aril 20 underline',command=chocolate_ball_window,padx=1000, highlightbackground=random.choice(colors))
basic_cookie_button = Button(window, text="Basic cookies", font='Aril 20 underline',command=basic_cookie_window,padx=1000, highlightbackground=random.choice(colors))
vintage_chocolate_chip_button = Button(window, text="vintage chocolate chip", font='Aril 20 underline',command=vintage_chocolate_chip_window,padx=1000, highlightbackground=random.choice(colors))
double_choc_peanut_butter_button = Button(window, text="Double choc peanut butter cookies ", font='Aril 20 underline',command=double_choc_peanut_butter_window,padx=1000, highlightbackground=random.choice(colors))
vegan_chocolate_chip_button = Button(window, text="Vegan chocolate chip cookies", font='Aril 20 underline',command=vegan_chocolate_chip_window,padx=1000, highlightbackground=random.choice(colors))
rainbow_cookies_button = Button(window, text="Rainbow cookies", font='Aril 20 underline',command=rainbow_cookies_window,padx=1000, highlightbackground=random.choice(colors))
cookies_extra_results_button = Button(window, text="Extra results from the recommended website according your search", font='Aril 25',command=cookies_extra_results, highlightbackground=random.choice(colors), height=4)



# Search, go agin button coomand function:
def go_agin():
    e.delete(0,1000000)
def s_command():
   s_input = e.get().split(" ")
   for inp in  s_input:
        for item in cookies:
            if inp == item:
                chocolate_ball_button.pack(side=BOTTOM)
                basic_cookie_button.pack(side=BOTTOM)
                vintage_chocolate_chip_button.pack(side=BOTTOM)
                double_choc_peanut_butter_button.pack(side=BOTTOM)
                vegan_chocolate_chip_button.pack(side=BOTTOM)
                rainbow_cookies_button.pack(side=BOTTOM)
                result_lable.pack(side=BOTTOM)
                cookies_extra_results_button.place(rely=0.40, relx=0.15)
                break
        for item in Vegetables:
            if inp == item:




                break
        else:continue
        break


# Search and Go agin Button############
S_button = Button(window, text="Search", font='Arial 22', width=8, command=s_command)
S_button.place(rely=0.25, relx=0.48)
G_agin_button = Button(window, text="Clear", font='Arial 22', width=8, command=go_agin)
G_agin_button.place(rely=0.25, relx=0.34)




window.mainloop()