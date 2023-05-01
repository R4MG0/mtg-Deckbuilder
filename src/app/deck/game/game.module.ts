import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import {MatMenuModule} from '@angular/material/menu';
import { GameRoutingModule } from './game-routing.module';
import { GameComponent } from './game.component';
import { LibraryComponent } from './components/library/library.component';
import { MatListModule} from '@angular/material/list';
import { MatIconModule} from '@angular/material/icon';
import { GraveyardComponent } from './components/graveyard/graveyard.component';
import {DragDropModule} from '@angular/cdk/drag-drop';



@NgModule({
  declarations: [
    GameComponent,
    LibraryComponent,
    GraveyardComponent
  ],
  imports: [
    CommonModule,
    GameRoutingModule,
    MatMenuModule,
    MatListModule,
    MatIconModule,
    DragDropModule
  ]
})
export class GameModule { }
