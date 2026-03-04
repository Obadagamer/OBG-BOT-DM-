import discord
import asyncio
import os
import sys
from colorama import Fore, Style, init

init(autoreset=True)

# لوحة الألوان الفاخرة
G, R, C, Y, M, W, B = Fore.GREEN, Fore.RED, Fore.CYAN, Fore.YELLOW, Fore.MAGENTA, Fore.WHITE, Fore.BLUE

class OBG_Ultimate(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_active = False
        self.current_channel = None

    def draw_banner(self):
        os.system('clear')
        banner = f"""
{C}    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
{C}    ┃ {M} ██████╗ ██████╗  ██████╗     ██████╗ ███╗   ███╗{C}  ┃
{C}    ┃ {M}██╔═══██╗██╔══██╗██╔════╝     ██╔══██╗████╗ ████║{C}  ┃
{C}    ┃ {M}██║   ██║██████╔╝██║  ███╗    ██║  ██║██╔████╔██║{C}  ┃
{C}    ┃ {M}██║   ██║██╔══██╗██║   ██║    ██║  ██║██║╚██╔╝██║{C}  ┃
{C}    ┃ {M}╚██████╔╝██████╔╝╚██████╔╝    ██████╔╝██║ ╚═╝ ██║{C}  ┃
{C}    ┃ {M} ╚═════╝ ╚═════╝  ╚═════╝     ╚═════╝ ╚═╝     ╚═╝{C}  ┃
{C}    ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
{C}    ┃ {W}SYSTEM: {G}ULTIMATE V2.0           {R}BY: {G}OBG STUDIO {C}┃
{C}    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        """
        print(banner)

    async def on_ready(self):
        await self.main_menu()

    async def main_menu(self):
        self.is_active = False
        self.draw_banner()
        print(f"{Y}[1] {W}PRIVATE DM BRIDGE (مراسلة شخص محدد)")
        print(f"{Y}[2] {W}MASS DM SENDER    (إرسال جماعي للأعضاء)")
        print(f"{Y}[3] {W}CHANNEL MONITOR   (مراقبة وإرسال في الرومات)")
        print(f"{R}[0] {W}LOGOUT / EXIT")
        print(f"{M}="*53)
        
        choice = input(f"{C}OBG_CONSOLE> {G}")
        
        if choice == '1': await self.handle_dm_bridge()
        elif choice == '2': await self.handle_mass_dm()
        elif choice == '3': await self.handle_channel_monitor()
        elif choice == '0': await self.close()
        else: await self.main_menu()

    # --- الخيار الأول: المراسلة الخاصة ---
    async def handle_dm_bridge(self):
        guild = await self.select_guild()
        if not guild: return await self.main_menu()
        
        members = [m for m in guild.members if not m.bot]
        print(f"{C}┌──────┬────────────────────────────────────────────┐")
        for i, m in enumerate(members):
            print(f"{C}│ {Y}{str(i).ljust(4)} {C}│ {W}{str(m).ljust(42)} {C}│")
        print(f"{C}└──────┴────────────────────────────────────────────┘")
        print(f"{R}[back] للعودة")
        
        choice = input(f"{M}[?]{W} Target ID: {G}")
        if choice.lower() == 'back': return await self.handle_dm_bridge()
        
        target = members[int(choice)]
        self.is_active = True
        self.current_target = target

        os.system('clear')
        print(f"{C}╔{'═'*50}╗")
        print(f"{C}║  {M}💬  {W}DM  {C}│  {G}{target.name.ljust(38)}{C}║")
        print(f"{C}╠{'═'*50}╣")
        print(f"{C}║  {Y}type 'back' to exit{' '*30}{C}║")
        print(f"{C}╚{'═'*50}╝\n")

        asyncio.create_task(self.chat_input_loop(target))

    # --- الخيار الثاني: إرسال جماعي ---
    async def handle_mass_dm(self):
        guild = await self.select_guild()
        if not guild: return await self.main_menu()
        
        msg = input(f"{M}[?]{W} Enter Message to Broadcast: {G}")
        print(f"{R}[!] Starting Mass DM... This may take time.")
        
        count = 0
        for member in guild.members:
            if not member.bot:
                try:
                    await member.send(msg)
                    print(f"{G}[+] Sent to: {member.name}")
                    count += 1
                    await asyncio.sleep(1) # لتجنب حظر الديسكورد
                except:
                    print(f"{R}[-] Failed: {member.name}")
        
        print(f"{Y}[✔] Completed. Sent to {count} members.")
        input(f"{W}Press Enter to return...")
        await self.main_menu()

    # --- الخيار الثالث: مراقبة الرومات ---
    async def handle_channel_monitor(self):
        guild = await self.select_guild()
        if not guild: return await self.main_menu()
        
        channels = [c for c in guild.text_channels]
        print(f"{C}┌──────┬────────────────────────────────────────────┐")
        for i, ch in enumerate(channels):
            print(f"{C}│ {Y}{str(i).ljust(4)} {C}│ {W}#{ch.name.ljust(41)} {C}│")
        print(f"{C}└──────┴────────────────────────────────────────────┘")
        
        choice = input(f"{M}[?]{W} Channel ID to Monitor: {G}")
        if choice.lower() == 'back': return await self.main_menu()
        
        self.current_channel = channels[int(choice)]
        self.is_active = True

        os.system('clear')
        print(f"{C}╔{'═'*50}╗")
        print(f"{C}║  {Y}#  {W}CHANNEL  {C}│  {G}{self.current_channel.name.ljust(35)}{C}║")
        print(f"{C}╠{'═'*50}╣")
        print(f"{C}║  {Y}type 'back' to exit{' '*30}{C}║")
        print(f"{C}╚{'═'*50}╝\n")

        asyncio.create_task(self.channel_input_loop())

    # --- أدوات مساعدة ---
    async def select_guild(self):
        self.draw_banner()
        guilds = list(self.guilds)
        for i, g in enumerate(guilds):
            print(f"{Y}[{i}] {W}{g.name}")
        print(f"{R}[back] Return to Menu")
        
        choice = input(f"{M}[?]{W} Select Server: {G}")
        if choice.lower() == 'back': return None
        return guilds[int(choice)]

    async def chat_input_loop(self, target):
        while self.is_active:
            content = await asyncio.get_event_loop().run_in_executor(
                None, input, f"{M} ❯❯ {W}"
            )
            if content.lower() == 'back':
                self.is_active = False
                await self.main_menu()
                break
            await target.send(content)

    async def channel_input_loop(self):
        while self.is_active:
            content = await asyncio.get_event_loop().run_in_executor(
                None, input, f"{M} ❯❯ {W}"
            )
            if content.lower() == 'back':
                self.is_active = False
                await self.main_menu()
                break
            await self.current_channel.send(content)

    async def on_message(self, message):
        if not self.is_active or message.author == self.user: return
        
        from datetime import datetime
        time = datetime.now().strftime("%H:%M")

        # عرض رسائل الخاص
        if self.current_target and message.author.id == self.current_target.id and isinstance(message.channel, discord.DMChannel):
            print(f"\n{C}┌─ {M}{message.author.name} {C}[{Y}{time}{C}]")
            print(f"{C}│  {W}{message.content}")
            print(f"{C}└{'─'*40}")
            
        # عرض رسائل الروم المراقب
        if self.current_channel and message.channel.id == self.current_channel.id:
            print(f"\n{C}┌─ {G}{message.author.name} {C}[{Y}{time}{C}] {C}│ {Y}#{message.channel.name}")
            print(f"{C}│  {W}{message.content}")
            print(f"{C}└{'─'*40}")

def start():
    os.system('clear')
    print(f"""
{C}    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
{C}    ┃ {M} ██████╗ ██████╗  ██████╗     ██████╗ ███╗   ███╗{C}  ┃
{C}    ┃ {M}██╔═══██╗██╔══██╗██╔════╝     ██╔══██╗████╗ ████║{C}  ┃
{C}    ┃ {M}██║   ██║██████╔╝██║  ███╗    ██║  ██║██╔████╔██║{C}  ┃
{C}    ┃ {M}██║   ██║██╔══██╗██║   ██║    ██║  ██║██║╚██╔╝██║{C}  ┃
{C}    ┃ {M}╚██████╔╝██████╔╝╚██████╔╝    ██████╔╝██║ ╚═╝ ██║{C}  ┃
{C}    ┃ {M} ╚═════╝ ╚═════╝  ╚═════╝     ╚═════╝ ╚═╝     ╚═╝{C}  ┃
{C}    ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
{C}    ┃ {W}SYSTEM: {G}ULTIMATE V2.0           {R}BY: {G}OBG STUDIO {C}┃
{C}    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    """)
    print(f"    {C}{'─'*52}")
    print(f"    {M}◆  {Y}AUTHENTICATION REQUIRED  {M}◆")
    print(f"    {C}{'─'*52}\n")
    token = input(f"    {M}╰─❯ {W}ENTER TOKEN {C}» {G}").strip()
    
    intents = discord.Intents.default()
    intents.members = True
    intents.message_content = True
    intents.presences = True

    client = OBG_Ultimate(intents=intents)
    try: client.run(token)
    except: print(f"{R}CRITICAL ERROR")

if __name__ == "__main__":
    start()
