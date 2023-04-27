import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-deck',
  templateUrl: './deck.component.html',
  styleUrls: ['./deck.component.scss']
})
export class DeckComponent {
  constructor(private readonly router: Router) { }
  toPlayTester() {
    this.router.navigate(['deck/game'])
  }
}
