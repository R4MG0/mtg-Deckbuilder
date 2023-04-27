import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { CommanderCard } from '../interfaces/commander-card';

@Injectable({
  providedIn: 'root'
})
export class ScryfallAPIService {

  constructor(private readonly http: HttpClient) { }

  getCardByName(cardName: string): CommanderCard {
    const card: CommanderCard = {} as CommanderCard;
    this.http.get(`https://api.scryfall.com/cards/named?fuzzy=${cardName}`).subscribe((cardData:any) => {
      card.uuid = cardData.id;
      card.name = cardData.name;
      card.cmc = cardData.cmc;
      card.colors = cardData.colors;
      card.colorIdentity = cardData.color_identity;
      card.image_uris = cardData.image_uris;
      card.keywords = cardData.keywords;
      card.mana_cost = cardData.mana_cost;
      card.power = cardData.power;
      card.toughness = cardData.toughness;

      console.log('response:', cardData);
    });
    return card
  }
}
