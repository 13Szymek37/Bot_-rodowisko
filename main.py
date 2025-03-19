import discord
from discord.ext import commands
description = '''Przykładowy bot , który pomoże ochronić środowisko.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def informacje(ctx):
    await ctx.send(f"Cześć nazywam się {bot.user} i jestem botem, który pomoże wam ochronić środowisko! Aby dowiedzieć się co oferuję wpisz ?commandlist")
@bot.command()
async def commandlist(ctx):
    await ctx.send(f'Lista komend to : recykling, zanieczyszczenia, rozkład, własny_pomysł, nie zapomnij przed każdą z nich wpisać --> ? <--')

@bot.command()
async def recykling(ctx):
    await ctx.send(f'Recykling oznacza ponowne użycie, powrót do obiegu.Pełną definicje oraz informacje o recyklingu znajdziesz tutaj : https://stat.gov.pl/metainformacje/slownik-pojec/pojecia-stosowane-w-statystyce-publicznej/1182,pojecie.html')

@bot.command()
async def zanieczyszczenia(ctx):
    await ctx.send(f'Zanieczyszczenia to bardzo obszerny temat.Oto kilka komend, które pomogą Ci zgłębić się w tym temacie : powietrze, wody_powierzchniowe, wody_glebowe')
@bot.command()
async def powietrze(ctx):
    await ctx.send(f'Zanieczyszczenie powietrza to obecność szkodliwych substancji w atmosferze ziemskiej, by dowiedzieć się o tym więcej zapraszam na tę strone : https://airly.org/pl/wszystko-co-powinienes-wiedziec-o-zanieczyszczeniu-powietrza/')
@bot.command()
async def wody_powierzchniowe(ctx):
    await ctx.send(f'Zanieczyszczenie wód powierzchniowych to widoczny problem polegający na dostawaniu się szkodliwych substancji do rzek i jezior po więcej informacji zajrzyj tutaj : https://www.filtrybb.pl/blog/42/skutki-zanieczyszczenia-wod')
@bot.command()
async def wody_glebowe(ctx):
    await ctx.send(f'Zanieczyszczenie wód glebowych to bardzo niebezpieczne, bo niewidoczne zjawisko po więcej informacji sprawdź te strone : https://retencja.pl/blog/zanieczyszczenie-wod-podziemnych/')
@bot.command()
async def rozkład(ctx):
    await ctx.send(f'Gdy wyrzucamy jakiś przedmiot to ulega on rozkładowi od jabłka, które rozłoży się w kilka tygodni, do reklamówek, które rozłożą sie za setki lat po więcej informacji zajrzyj tu : https://www.decathlon.pl/c/misc/jak-dlugo-rozkladaja-sie-smieci-czas-rozkladu-roznych-odpadow_974d3bdc-cafc-4508-a85e-a5475824fe52')
@bot.command()
async def własny_pomysł(ctx):
    await ctx.send(f'Jeśli posiadasz pomysł jak mogę udosklkonalić mojego bota lub jakie komendy mogę dodać skontaktuj się ze mną tutaj : adszymek2020@gmail.com') 
bot.run('token')
