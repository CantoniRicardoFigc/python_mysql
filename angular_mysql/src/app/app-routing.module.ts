import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ChiamataComponent } from './chiamata/chiamata.component';

const routes: Routes = [
  {path: '', component: ChiamataComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
