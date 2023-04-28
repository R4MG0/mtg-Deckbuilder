import { Component, EventEmitter, HostListener, Input, OnInit, Output, ViewChild } from '@angular/core';
import { MatMenuTrigger } from '@angular/material/menu';
import { Card } from 'src/app/shared/interfaces/card';

@Component({
  selector: 'app-library',
  templateUrl: './library.component.html',
  styleUrls: ['./library.component.scss']
})
export class LibraryComponent implements OnInit {
  @Input() deck: Card[] = [];
  @Output() newCard = new EventEmitter<Card>();
  reveal = false;

constructor() {
}

ngOnInit(): void {
}
 @HostListener("click", ["$event"])
  onClick() {
    this.draw();
    // this.newCard.emit({
    //   id:9,
    //   name: 'Forest',
    //   img: 'https://cards.scryfall.io/normal/front/8/0/80716ed1-8d0e-44e6-8b18-606e80d22181.jpg?1682205975',
    //   type: 'Basic Land',
    //   deck: 'Commander',
    //   controller: 'Player 1'
    // })
  }
draw(){
    this.newCard.emit(this.deck[0]);
}
revealTopCard() {
  this.reveal = true;
  setTimeout(() => {
    this.reveal = false;
  }, 5000);

}

  @ViewChild(MatMenuTrigger)
  contextMenu: MatMenuTrigger  = {} as MatMenuTrigger;

  contextMenuPosition = { x: '0px', y: '0px' };

  onContextMenu(event: MouseEvent, item?: Item) {
    event.preventDefault();
    this.contextMenuPosition.x = event.clientX + 'px';
    this.contextMenuPosition.y = event.clientY + 'px';
    this.contextMenu.menuData = { 'item': item };
    this.contextMenu.menu?.focusFirstItem('mouse');
    this.contextMenu.openMenu();
  }




  onContextMenuAction3() {
    alert(`Search Library`);
  }
  onContextMenuAction4() {
    alert(`Shuffle Library`);
  }
  onContextMenuAction5() {
    alert(`Mill X cards`);
  }

  getImageSrcOfTopCardOfLibrary() {
    return this.deck[0].img;
  }
}

export interface Item {
  id: number;
  name: string;
}
