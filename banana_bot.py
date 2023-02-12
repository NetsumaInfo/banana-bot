import discord
from discord.ext import tasks, commands
import os
import interactions
from interactions import Intents
from discord.utils import get
from dotenv import load_dotenv
import asyncio

intents = Intents(8)
intents.message_content = True
intents.guild_messages = True
intents.guild_reactions = True
intents.guild_scheduled_events = True
intents.guild_typing = True
intents.guilds = True
intents.presences = True
#For a more secure, we loaded the .env file and assign the token value to a variable 
load_dotenv(".env")

bot = interactions.Client(
    token = os.getenv("TOKEN"),
    intents=intents)


CHOICE_project = []

@bot.event
async def on_ready():
    print("bot ready")


@bot.command(
    name="tache-fini",
    description="signaler que vous avez fini une tache.",
    scope=1062737741802131568,
    options=[
        interactions.Option(
            name="ping",
            description="l'utilisateur a pign pour la prochaine tache",
            type=interactions.OptionType.USER,
            required=True,
        ),
        interactions.Option(
            name="projet",
            description="le nom du projet",
            type=interactions.OptionType.STRING,
            required=True,
            #value="choice_one",
            choices=[
                interactions.Choice(name="Dungeon Kurashi No Moto Yuusha", value="Dungeon Kurashi No Moto Yuusha"),
                interactions.Choice(name="Daddy From Hell",value="Daddy From Hell"),
                interactions.Choice(name="Shijou Saikyou no Mahou Kenshi, F Rank Boukensha ni Tensei Suru",value="Shijou Saikyou no Mahou Kenshi, F Rank Boukensha ni Tensei Suru"),
                interactions.Choice(name="Killmax 2.0",value="Killmax 2.0"),
                interactions.Choice(name="Shiikuin-San Wa Isekai De Doubutsuen Tsukuritainode Monsutaa Wo Tenazukeru",value="Shiikuin-San Wa Isekai De Doubutsuen Tsukuritainode Monsutaa Wo Tenazukeru"),
                interactions.Choice(name="Kamigami ni Sodaterare Shimo no, Saikyou to Naru",value="Kamigami ni Sodaterare Shimo no, Saikyou to Naru"),
                interactions.Choice(name="Shindou Yuusha to Maid Onee-san",value="Shindou Yuusha to Maid Onee-san"),
                interactions.Choice(name="Hyakuren no Haou to Seiyaku no Ikusa Otome",value="Hyakuren no Haou to Seiyaku no Ikusa Otome"),
                interactions.Choice(name="Grand Général",value="Grand Général"),
                interactions.Choice(name="My Girlfriend Cheated on Me With a Senior, so I’m Cheating on Her With His Girlfriend",value="My Girlfriend Cheated on Me With a Senior, so I’m Cheating on Her With His Girlfriend"),
                interactions.Choice(name="Return of the Invincible Patriarch",value="Return of the Invincible Patriarch"),
                interactions.Choice(name="High School Taoist",value="High School Taoist"),
                interactions.Choice(name="Teenage Swordsman",value="Teenage Swordsman"),
                interactions.Choice(name="Magician from Another World",value="Magician from Another World"),
                interactions.Choice(name="Maou desu.",value="Maou desu."),
                interactions.Choice(name="I Have Twin Girfriends",value="I Have Twin Girfriends"),
                interactions.Choice(name="Maou Gakuen no Hangyakusha",value="Maou Gakuen no Hangyakusha"),
                interactions.Choice(name="Isekai Monster Breeder",value="Isekai Monster Breeder"),
                ],
            #autocomplete=True,
        ),
        interactions.Option(
            name="chapitre",
            description="le numéro du chapitre",
            type=interactions.OptionType.INTEGER,
            required=True,
        ),
        interactions.Option(
            name="poste",
            description="quelle genre de travail avez-vous fait?",
            type=interactions.OptionType.STRING,
            required=True,
            choices=[
                #interactions.Choice(name="Choose me! :(", value="choice_one"),
                    interactions.Choice(name="Raw",value="Raw"),             
                    interactions.Choice(name="Trad",value="Trad"),            
                    interactions.Choice(name="Clean",value="Clean"),           
                    interactions.Choice(name="Reco",value="Reco"),            
                    interactions.Choice(name="Clean et Reco",value="Clean et Reco"),
                    interactions.Choice(name="Check",value="Check"),           
                    interactions.Choice(name="Edit",value="Edit"),            
                    interactions.Choice(name="Q-Check",value="Q-Check"),         
                    interactions.Choice(name="Q-Edit",value="Q-Edit"),
                    interactions.Choice(name="Q-Clean",value="Q-Clean"),
                    interactions.Choice(name="Q-Reco",value="Q-Reco")
                ],
        ),
    ]
)
async def tache_fini(ctx: interactions.CommandContext,
                     ping,
                     projet:str,
                     chapitre:int,
                     poste:str,
                     fichier=None):
    print(f"<@{ping.id}>\t> <@{ctx.author.id}> a terminer de **{poste}**\t> Le chapitre **{chapitre}** de **{projet}**")
    if fichier is not None:
        await ctx.send(files=[fichier])
    await ctx.send(f"vous evez transmis avec succes, merci", ephemeral=True)
    await ctx.send(f"<@{ping.id}>\n> <@{ctx.author.id}> a terminer de **{poste}**\n> Le chapitre **{chapitre}** de **{projet}**")

#Run the bot
bot.start()
