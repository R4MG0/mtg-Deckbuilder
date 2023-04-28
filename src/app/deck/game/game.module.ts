import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import {MatMenuModule} from '@angular/material/menu';
import { GameRoutingModule } from './game-routing.module';
import { GameComponent } from './game.component';
import { LibraryComponent } from './components/library/library.component';
import { MatListModule} from '@angular/material/list';
import { MatIconModule} from '@angular/material/icon';


@NgModule({
  declarations: [
    GameComponent,
    LibraryComponent
  ],
  imports: [
    CommonModule,
    GameRoutingModule,
    MatMenuModule,
    MatListModule,
    MatIconModule
  ]
})
export class GameModule { }
