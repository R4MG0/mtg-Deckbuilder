import { Component, OnInit } from '@angular/core';
import { ScryfallAPIService } from 'src/app/shared/services/scryfall-api.service';
import { Card } from 'src/app/shared/interfaces/card';

@Component({
  selector: 'app-game',
  templateUrl: './game.component.html',
  styleUrls: ['./game.component.scss']
})
export class GameComponent implements OnInit {
  deck: Card[] = [];
  hand: Card[] = [];
  link = 'https://static.wikia.nocookie.net/mtgsalvation_gamepedia/images/f/f8/Magic_card_back.jpg/revision/latest?cb=20140813141013'

  constructor(private readonly scryfallService: ScryfallAPIService){}
  ngOnInit(): void {
    const arrCards = this.scryfallService.getDeck();
    for(let i =0; i<7; i++){
      this.hand.push(arrCards[i]);
      // arrCards.splice(0,i);
    }
    // this.deck.push(...arrCards);
    console.log('hand:', this.hand);

  }
  test(){
    alert();
  }
}
