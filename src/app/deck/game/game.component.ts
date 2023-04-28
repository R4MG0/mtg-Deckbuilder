import { Component, OnInit } from '@angular/core';
import { ScryfallAPIService } from 'src/app/shared/services/scryfall-api.service';
import { Card } from 'src/app/shared/interfaces/card';

@Component({
  selector: 'app-game',
  templateUrl: './game.component.html',
  styleUrls: ['./game.component.scss']
})
export class GameComponent implements OnInit {
  library: Card[] = [];
  hand: Card[] = [];
  commanderZone = false;
  graveyardZone = true;
  link = 'https://static.wikia.nocookie.net/mtgsalvation_gamepedia/images/f/f8/Magic_card_back.jpg/revision/latest?cb=20140813141013'

  constructor(private readonly scryfallService: ScryfallAPIService){}

  ngOnInit(): void {
  const arrCards = this.scryfallService.getDeck();
  this.library = arrCards;
  for(let i = 0; i < 7; i++) {
    this.hand.push(this.library.shift() as Card); // remove first card from library and add it to hand
  }
}
  commanderAvailable(){
    this.commanderZone != this.commanderZone;
  }
  graveyardAvailable(){
    this.graveyardZone != this.graveyardZone;
  }
  onChangeHand(card: Card) {
    this.hand.push(card);
    this.library.shift();
    // console.log('library: ', this.library)
    this.library.push(this.scryfallService.getCardByName('plains', 'card') as Card);
  }
}
