import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { AppComponent } from './app.component';
import { ChiamataComponent } from './chiamata/chiamata.component';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';

@NgModule({
  declarations: [
    // ...
    AppComponent,
    ChiamataComponent
  ],
  imports: [
    HttpClientModule,
    BrowserModule,
    AppRoutingModule
    // ...
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
