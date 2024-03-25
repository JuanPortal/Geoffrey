from discord.ext import commands
import discord
import os
import random

client = commands.Bot(command_prefix="$", intents=discord.Intents.all())
client.remove_command("help")


@client.event
async def on_ready():
    print("Geoffrey's ready to go!")


@client.command(pass_context=True, aliases=['i', 'info'])
async def dox(ctx, *, arg):
    try:
        if arg not in [str(member.name) for member in ctx.guild.members]:
            await ctx.send("Member not found")
            return
        
        member = discord.utils.get(ctx.guild.members, name=arg)

        embed = discord.Embed(title="User Information", color=discord.Color(0xFFFFFF))
        embed.set_thumbnail(url=member.avatar)
        embed.add_field(name="Username", value=member.name, inline=True)
        embed.add_field(name="Discriminator", value=member.discriminator, inline=True)
        embed.add_field(name="ID", value=member.id, inline=True)
        embed.add_field(name="Status", value=member.status, inline=True)
        embed.add_field(name="Top Role", value=member.top_role.name, inline=True)
        embed.add_field(name="Joined Server", value=member.joined_at.strftime("%A, %B %d %Y %I:%M %p"), inline=True)
        embed.add_field(name="Joined Discord", value=member.created_at.strftime("%A, %B %d %Y %I:%M %p"), inline=True)
        await ctx.send(embed=embed)

    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")


@client.command()
async def members(ctx):
    members = ctx.guild.members
    member_list = ''
    for member in members:
        member_list += str(member.name) + '      (' + str(member.display_name) + ')' + '\n'
    embed = discord.Embed(title="Members", color=discord.Color(0xFFFFFF), description=member_list)
    await ctx.send(embed=embed)


@client.command(pass_context=True, aliases=['monopolio', 'equipo', 'pais', 'paises', 'team'])
async def monopoly(ctx, *args):
    n = len(args)
    
    if n % 2 != 0 or n < 2:
        await ctx.send("Ingresa número par")
        return

    friends = list(args)[:n//2]
    countries = list(args)[n//2:]
    random.shuffle(countries)

    assignments = {}
    for friend, country in zip(friends, countries):
        assignments[friend] = country

    assignment_text = "\n".join([f"{friend}: {assigned_country}" for friend, assigned_country in assignments.items()])
    await ctx.send(f"{assignment_text}")


@client.command(pass_context=True, aliases=['t'])
async def test(ctx):
    await ctx.send('$wotd')
    await ctx.send('$cd 00:02')
    await ctx.send('$meme')
    await ctx.send('$psv')


@client.command(pass_context=True, aliases=['moneda'])
async def flipcoin(ctx):
    await ctx.send(random.choice(['heads', 'tails']))


@client.command(pass_context=True, aliases=['random'])
async def rng(ctx, number: int):
    await ctx.send(random.randint(1, int(number)))



@client.command(pass_context=True)
async def help(ctx):
    em = discord.Embed(
        title="Help",
        description=
        "***$dox*** *member*\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0member info\n\n***$members***\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0member list\n\n***$monopoly*** *player1 player2 country1 country2*\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0assigns a random country\n\n***$test***\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0tests other bots\n\n***$flipcoin***\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0heads or tails\n\n***$rng*** *number*\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0random number generator"
    )
    await ctx.send(embed=em)


client.run(os.environ["TOKEN"])