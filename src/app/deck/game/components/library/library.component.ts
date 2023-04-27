import { Component, EventEmitter, HostListener, Input, Output } from '@angular/core';
import { Card } from 'src/app/shared/interfaces/card';

@Component({
  selector: 'app-library',
  templateUrl: './library.component.html',
  styleUrls: ['./library.component.scss']
})
export class LibraryComponent {
  @Input() deck: Card[] = [];
  @Output() newCard = new EventEmitter<Card>();

constructor() { }
@HostListener("contextmenu", ["$event"])
  onRightClick(event: MouseEvent) {
    alert('right click');
    // event.preventDefault();
    // event.stopPropagation();
      // this.right_clickOnly = false;
  }
    @HostListener("click", ["$event"])
  onClick() {
    this.newCard.emit({
      id:9,
      name: 'Forest',
      img: 'https://cards.scryfall.io/normal/front/8/0/80716ed1-8d0e-44e6-8b18-606e80d22181.jpg?1682205975',
      type: 'Basic Land',
      deck: 'Commander',
      controller: 'Player 1'
    })
  }
}
