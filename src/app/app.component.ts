import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';
import { OnInit } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  title = 'deckBuilder';
  cards: any[] = [];
  commanders: any[] = [];

  constructor(private readonly http: HttpClient) {}

  ngOnInit(): void {
    this.http.get('https://api.magicthegathering.io/v1/cards').subscribe((data) => {
      this.cards.push(data);
    });
  }

  getCommander() {
    this.http.get('https://api.scryfall.com/cards/random?q=is%3Acommander').subscribe((data) => {
      this.commanders.push(data);
    });
  }


}
