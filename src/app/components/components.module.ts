import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { NotFoundComponent } from './not-found/not-found.component';



@NgModule({
  exports:[NotFoundComponent],
  declarations: [
    NotFoundComponent
  ],
  imports: [
    CommonModule
  ]
})
export class ComponentsModule { }
