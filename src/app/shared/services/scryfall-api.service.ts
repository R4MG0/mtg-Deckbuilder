import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { CommanderCard } from '../interfaces/commander-card';
import { Card } from '../interfaces/card';

@Injectable({
  providedIn: 'root',
})
export class ScryfallAPIService {
  constructor(private readonly http: HttpClient) {}

  getCardByName(
    cardName: string,
    typeOfResponse?: string
  ): CommanderCard | Card {
    const commanderCard: CommanderCard = {} as CommanderCard;
    const card: Card = {} as Card;
    this.http
      .get(`https://api.scryfall.com/cards/named?fuzzy=${cardName}`)
      .subscribe((cardData: any) => {
        if (typeOfResponse === 'commander') {
          commanderCard.uuid = cardData.id;
          commanderCard.name = cardData.name;
          commanderCard.cmc = cardData.cmc;
          commanderCard.colors = cardData.colors;
          commanderCard.colorIdentity = cardData.color_identity;
          commanderCard.image_uris = cardData.image_uris;
          commanderCard.keywords = cardData.keywords;
          commanderCard.mana_cost = cardData.mana_cost;
          commanderCard.power = cardData.power;
          commanderCard.toughness = cardData.toughness;
        } else {
          card.id = cardData.id;
          card.name = cardData.name;
          card.img = cardData.image_uris.normal;
          card.type = cardData.type_line;
          card.deck = 'Commander';
          card.controller = 'Player 1';
        }
      });
    if (typeOfResponse === 'commander') {
      return commanderCard as CommanderCard;
    }
    return card as Card;
  }

  changeCardPosition(card: Card, newZone: string) {
    this.http.post('http://localhost:3000/cardZoneChanged', card);
  }

  getDeck(): Card[] {
    const arr = [
      {
        id: 1,
        name: 'Shell of the Last Kappa',
        img: 'https://cards.scryfall.io/normal/front/4/d/4d80f3e7-c3f0-462f-8ae9-8b27a7c15fcd.jpg?1562759886',
        type: 'Legendary Artifact Creature',
        deck: 'Commander',
        controller: 'Player 1',
        // zone: 'Mainboard'
      },
      {
        id: 2,
        name: 'Lightning Bolt',
        img: 'https://cards.scryfall.io/normal/front/f/2/f29ba16f-c8fb-42fe-aabf-87089cb214a7.jpg?1673147852',
        type: 'Instant',
        deck: 'Commander',
        controller: 'Player 1',
      },
      {
        id: 3,
        name: 'Cordial Vampire',
        img: 'https://cards.scryfall.io/normal/front/8/c/8c84150f-e2bf-42a2-b2f7-2b6004b29fa4.jpg?1641602498',
        type: 'creature',
        deck: 'Commander',
        controller: 'Player 1',
      },
      {
        id: 4,
        name: 'Trelasarra, Moon Dancer',
        img: 'https://cards.scryfall.io/normal/front/f/6/f6a4b54c-a8fa-464e-a3dd-f3f3a08606f5.jpg?1627709553',
        type: 'Legendary Creature',
        deck: 'Commander',
        controller: 'Player 1',
      },
      {
        id: 5,
        name: 'Angelfire Ignition',
        img: 'https://cards.scryfall.io/normal/front/8/b/8ba4c7a2-6243-43ed-8c1c-e3edee43a583.jpg?1636225070',
        type: 'Sorcery',
        deck: 'Commander',
        controller: 'Player 1',
      },
      {
        id: 6,
        name: 'Arbor Elf',
        img: 'https://cards.scryfall.io/normal/front/4/b/4b81165e-f091-4211-8b47-5ea6868b0d4c.jpg?1562435427',
        type: 'Creature',
        deck: 'Commander',
        controller: 'Player 1',
      },
      {
        id: 7,
        name: 'Cruel Fate',
        img: 'https://cards.scryfall.io/normal/front/4/4/44bea0d4-946e-4cb8-b6f1-50231d52bfbe.jpg?1562446619',
        type: 'Sorcery',
        deck: 'Commander',
        controller: 'Player 1',
      },
      {
        id: 8,
        name: 'Demonic Tutor',
        img: 'https://cards.scryfall.io/normal/front/3/b/3bdbc231-5316-4abd-9d8d-d87cff2c9847.jpg?1618695728',
        type: 'Sorcery',
        deck: 'Commander',
        controller: 'Player 1',
      },
      {
        id: 9,
        name: 'Shell of the Last Kappa',
        img: 'https://cards.scryfall.io/normal/front/4/d/4d80f3e7-c3f0-462f-8ae9-8b27a7c15fcd.jpg?1562759886',
        type: 'Legendary Artifact Creature',
        deck: 'Commander',
        controller: 'Player 1',
      },
      {
        id: 10,
        name: 'Lightning Bolt',
        img: 'https://cards.scryfall.io/normal/front/f/2/f29ba16f-c8fb-42fe-aabf-87089cb214a7.jpg?1673147852',
        type: 'Instant',
        deck: 'Commander',
        controller: 'Player 1',
      },
      {
        id: 11,
        name: 'Cordial Vampire',
        img: 'https://cards.scryfall.io/normal/front/8/c/8c84150f-e2bf-42a2-b2f7-2b6004b29fa4.jpg?1641602498',
        type: 'creature',
        deck: 'Commander',
        controller: 'Player 1',
      },
      {
        id: 12,
        name: 'Trelasarra, Moon Dancer',
        img: 'https://cards.scryfall.io/normal/front/f/6/f6a4b54c-a8fa-464e-a3dd-f3f3a08606f5.jpg?1627709553',
        type: 'Legendary Creature',
        deck: 'Commander',
        controller: 'Player 1',
      },
      {
        id: 13,
        name: 'Angelfire Ignition',
        img: 'https://cards.scryfall.io/normal/front/8/b/8ba4c7a2-6243-43ed-8c1c-e3edee43a583.jpg?1636225070',
        type: 'Sorcery',
        deck: 'Commander',
        controller: 'Player 1',
      },
      {
        id: 14,
        name: 'Arbor Elf',
        img: 'https://cards.scryfall.io/normal/front/4/b/4b81165e-f091-4211-8b47-5ea6868b0d4c.jpg?1562435427',
        type: 'Creature',
        deck: 'Commander',
        controller: 'Player 1',
      },
      {
        id: 15,
        name: 'Cruel Fate',
        img: 'https://cards.scryfall.io/normal/front/4/4/44bea0d4-946e-4cb8-b6f1-50231d52bfbe.jpg?1562446619',
        type: 'Sorcery',
        deck: 'Commander',
        controller: 'Player 1',
      },
      {
        id: 16,
        name: 'Demonic Tutor',
        img: 'https://cards.scryfall.io/normal/front/3/b/3bdbc231-5316-4abd-9d8d-d87cff2c9847.jpg?1618695728',
        type: 'Sorcery',
        deck: 'Commander',
        controller: 'Player 1',
      },
    ];
    return arr;
  }
}
