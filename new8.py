
import sys
import random
from colorama import Fore, Style, init

init(autoreset=True)


def main():
    print(
        f"\n{Fore.CYAN}{Style.BRIGHT}Welcome to Blackjack by Bilawal!{Style.RESET_ALL}")
    name = input("\nEnter your name: ")

    print(
        f"\nHello {Fore.YELLOW}{name}{Style.RESET_ALL}! Do you want to play?\n")
    print(f"{Fore.RED}1){Style.RESET_ALL} Yes")
    print(f"{Fore.RED}2){Style.RESET_ALL} No / leave")

    choice = input("\nEnter 1 or 2 : ")
    while choice not in ["1", "2"]:
        choice = input(
            f"\n{Fore.RED}Please enter 1 for playing or 2 for leaving: {Style.RESET_ALL}")

    if choice == "2":
        print(
            f"\n{Fore.YELLOW}{Style.BRIGHT}Bye, have a good day !!!{Style.RESET_ALL}")
        sys.exit()

    player_wins = 0
    dealer_wins = 0
    ties = 0

    while True:
        deck = create_deck()
        deck_items = list(shuffle(deck).items())
        print(f"\n{Fore.CYAN}--- Shuffling and drawing cards ---{Style.RESET_ALL}")

        dealer_hand = [deck_items.pop(), deck_items.pop()]
        player_hand = [deck_items.pop(), deck_items.pop()]

        while True:
            player_score = calculate_hand_score(player_hand)
            print(f"\n{Fore.GREEN}--- {name.upper()} ---{Style.RESET_ALL}")
            print(
                f"Your hand : {', '.join([card[0] for card in player_hand])}")
            print(f"Score     : {player_score}")

            print(f"\n{Fore.GREEN}--- DEALER ---{Style.RESET_ALL}")
            print(
                f"Dealer hand : {dealer_hand[0][0]}, {Fore.BLACK}Hidden{Style.RESET_ALL}")

            if player_score > 21:
                print(
                    f"Dealer reveals: {', '.join([card[0] for card in dealer_hand])}")
                break

            move = input(
                f"\nSo hit or stand? ").lower().strip()
            if move == 'hit':
                player_hand.append(deck_items.pop())
            elif move == 'stand':
                break
            else:
                print(
                    f"{Fore.RED}Invalid choice! Please type 'hit' or 'stand'.{Style.RESET_ALL}")

        player_score = calculate_hand_score(player_hand)
        dealer_score = calculate_hand_score(dealer_hand)

        if player_score <= 21:
            print(f"\n{Fore.GREEN}--- DEALER'S TURN ---{Style.RESET_ALL}")
            print(
                f"Dealer reveals: {', '.join([card[0] for card in dealer_hand])}")

            while dealer_score < 17:
                new_card = deck_items.pop()
                dealer_hand.append(new_card)
                dealer_score = calculate_hand_score(dealer_hand)
                print(
                    f"Dealer drew: {new_card[0]}. Total: {dealer_score}")

        result = determine_winner(player_score, dealer_score, name)

        if result == "player":
            player_wins += 1
        elif result == "dealer":
            dealer_wins += 1
        else:
            ties += 1

        print(f"\n{Style.BRIGHT}Stats: Wins: {Fore.GREEN}{player_wins}{Style.RESET_ALL} | "
              f"Losses: {Fore.RED}{dealer_wins}{Style.RESET_ALL} | Ties: {Fore.YELLOW}{ties}{Style.RESET_ALL}")

        if not ask_to_play_again(name):
            break


def create_deck():
    suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
    cards = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
        'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11
    }
    deck = {}
    for suit in suits:
        for card, value in cards.items():
            deck[f'{card} of {suit}'] = value
    return deck


def shuffle(deck):
    shuffled_items = list(deck.items())
    random.shuffle(shuffled_items)
    return dict(shuffled_items)


def calculate_hand_score(hand):
    score = sum(card[1] for card in hand)
    aces = sum(1 for card in hand if "Ace" in card[0])
    while score > 21 and aces > 0:
        score -= 10
        aces -= 1
    return score


def determine_winner(player_score, dealer_score, name):
    print(f"\n{Fore.CYAN}--- Final Results ---{Style.RESET_ALL}")
    print(f"{name}'s Score: {player_score}")
    print(f"Dealer Score: {dealer_score}")
    print("-" * 21)

    if player_score > 21:
        print(f"{Fore.RED}Result: You Busted! Dealer wins.{Style.RESET_ALL}")
        return "dealer"
    elif dealer_score > 21:
        print(f"{Fore.GREEN}Result: Dealer Busted! You win!{Style.RESET_ALL}")
        return "player"
    elif player_score > dealer_score:
        print(f"{Fore.GREEN}Result: You win!{Style.RESET_ALL}")
        return "player"
    elif dealer_score > player_score:
        print(f"{Fore.RED}Result: Dealer wins!{Style.RESET_ALL}")
        return "dealer"
    else:
        print(f"{Fore.YELLOW}Result: It's a tie!{Style.RESET_ALL}")
        return "tie"


def ask_to_play_again(name):
    while True:
        choice = input(
            f"\nWant to play another round? [yes or no]: ").lower()
        if choice == "yes":
            return True
        if choice == "no":
            print(
                f"\n{Fore.YELLOW}{Style.BRIGHT}Thanks for playing, {name}! Have a great day!{Style.RESET_ALL}")
            return False
        print(f"{Fore.RED}Please enter 'yes' or 'no'.{Style.RESET_ALL}")


if __name__ == "__main__":
    main()
