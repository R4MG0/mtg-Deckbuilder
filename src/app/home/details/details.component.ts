import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { CommanderCard } from 'src/app/shared/interfaces/commander-card';
import { ScryfallAPIService } from 'src/app/shared/services/scryfall-api.service';

@Component({
  templateUrl: './details.component.html',
  styleUrls: ['./details.component.scss']
})
export class DetailsComponent implements OnInit{
  cardName: string = '';
  card!: CommanderCard;
  displayNotFound: boolean = false;

  constructor(private readonly route: ActivatedRoute, private readonly scryfallApiService: ScryfallAPIService) { }
  ngOnInit(): void {
    this.cardName = String(this.route.snapshot.paramMap.get('cardName'));
    this.card = this.scryfallApiService.getCardByName(this.cardName);

  }
}
