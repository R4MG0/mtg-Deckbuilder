import { Component } from '@angular/core';
import { CommanderCard } from '../shared/interfaces/commander-card';
import { HttpClient } from '@angular/common/http';
import { FormControl, FormGroup } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent {
title = 'deckBuilder';
  cards: any[] = [];
  commanders: CommanderCard[] = [];
  searchedCard: CommanderCard = {} as CommanderCard;
  form = new FormGroup({
    nameOfCard: new FormControl(''),
  })

  constructor(private readonly http: HttpClient, private readonly router: Router) {}

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
    if(this.form.value.nameOfCard === '') return alert('you have to enter a card name');
    this.router.navigate([`home/detail/${this.form.value.nameOfCard}`]);
    // this.http.get('https://api.scryfall.com/cards/named?fuzzy=aust+com').subscribe(
    //   (data: any) => {
    //     this.searchedCard = {
    //       uuid: data.id,
    //       name: data.name,
    //       cmc: data.cmc,
    //       colors: data.colors,
    //       colorIdentity: data.color_identity,
    //       image_uris: data.image_uris,
    //       keywords: data.keywords,
    //       mana_cost: data.mana_cost,
    //       power: data.power,
    //       toughness: data.toughness
    //     };
    //     console.log('searched card: ', this.searchedCard);

    // })
  }


}
