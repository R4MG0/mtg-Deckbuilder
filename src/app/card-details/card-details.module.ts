import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { CardDetailsRoutingModule } from './card-details-routing.module';
import { CardDetailsComponent } from './card-details.component';


@NgModule({
  declarations: [
    CardDetailsComponent
  ],
  imports: [
    CommonModule,
    CardDetailsRoutingModule
  ]
})
export class CardDetailsModule { }
