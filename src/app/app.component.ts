import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';
import { OnInit } from '@angular/core';
import { CommanderCard } from './shared/interfaces/commander-card';
import { FormControl, FormGroup } from '@angular/forms';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  title = 'deckBuilder';
  cards: any[] = [];
  commanders: CommanderCard[] = [];
  form = new FormGroup({
    nameOfCard: new FormControl(''),
  })

  constructor(private readonly http: HttpClient) {}

  ngOnInit(): void {
    this.http.get('https://api.magicthegathering.io/v1/cards').subscribe((data) => {
      this.cards.push(data);
    });
  }

  getCommander() {
    this.http.get('https://api.scryfall.com/cards/random?q=is%3Acommander').subscribe((data: any) => {
      const card: CommanderCard = {
        uuid: data.id,
        name: data.name,
        cmc: data.cmc,
        colors: data.colors,
        colorIdentity: data.color_identity,
        image_uris: data.image_uris,
        keywords: data.keywords,
        mana_cost: data.mana_cost,
        power: data.power,
        toughness: data.toughness
      };
      this.commanders.push(card);
      console.log(this.commanders);
    });
  }

  submit() {
    alert('submit')
  }


}
