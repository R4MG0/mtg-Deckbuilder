import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { NotFoundComponent } from './not-found/not-found.component';
import { NavigationComponent } from './navigation/navigation.component';



@NgModule({
  exports:[NotFoundComponent, NavigationComponent],
  declarations: [
    NotFoundComponent,
    NavigationComponent
  ],
  imports: [
    CommonModule
  ]
})
export class ComponentsModule { }
