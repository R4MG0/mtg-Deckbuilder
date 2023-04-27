import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home.component';
import { DetailsComponent } from './details/details.component';

const routes: Routes = [{ path: '', component: HomeComponent },
  // { path: '/:cardName/details', loadChildren: () => import('../card-details/card-details.module').then(m => m.CardDetailsModule) }];
  // { path: 'detail/cardName', loadChildren: () => import('../card-details/card-details.module').then(m => m.CardDetailsModule)}
  {path: 'detail/:cardName', component: DetailsComponent}
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class HomeRoutingModule { }
