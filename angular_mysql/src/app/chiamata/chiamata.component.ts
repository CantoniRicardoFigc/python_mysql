import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';
import { Observable } from 'rxjs';
import { Root, Root2 } from '../app.model';

@Component({
  selector: 'app-chiamata',
  templateUrl: './chiamata.component.html',
  styleUrls: ['./chiamata.component.css']
})
export class ChiamataComponent {

  obsCard !: Observable<Root>;
  ris !: Root;
  obsCard1 !: Observable<Root>;
  ris1 !: Root;
  obsCard2 !: Observable<Root>;
  ris2 !: Root;
  obsCard3 !: Observable<Root>;
  ris3 !: Root;
  obsCard4 !: Observable<Root>;
  ris4 !: Root;

  constructor(private http : HttpClient) {}

  ricercaGetAllData() {
    this.obsCard = this.http.get<Root>('https://5000-cantonirica-pythonmysql-xmm0bj5789h.ws-eu107.gitpod.io/getAllDataInHtml')
    this.obsCard.subscribe(
      (data : Root)=>
      {
        this.ris = (data);
        console.log(data)
      })
  }

  ricercaCount() {
    this.obsCard1 = this.http.get<Root>('https://5000-cantonirica-pythonmysql-xmm0bj5789h.ws-eu107.gitpod.io/count')
    this.obsCard1.subscribe(
      (data : Root)=>
      {
        this.ris1 = (data);
        console.log(data)
      })
  }
  
  ricercaAirTransport() {
    this.obsCard2 = this.http.get<Root>('https://5000-cantonirica-pythonmysql-xmm0bj5789h.ws-eu107.gitpod.io/air_transport')
    this.obsCard2.subscribe(
      (data : Root)=>
      {
        this.ris2 = (data);
        console.log(data)
      })
  }

  ricercaEpicUnits() {
    this.obsCard3 = this.http.get<Root>('https://5000-cantonirica-pythonmysql-xmm0bj5789h.ws-eu107.gitpod.io/epic_units')
    this.obsCard3.subscribe(
      (data : Root)=>
      {
        this.ris3 = (data);
        console.log(data)
      })
  }

  ricercaCardCost() {
    this.obsCard4 = this.http.get<Root>('https://5000-cantonirica-pythonmysql-xmm0bj5789h.ws-eu107.gitpod.io/card_cost')
    this.obsCard4.subscribe(
      (data : Root)=>
      {
        this.ris4 = (data);
        console.log(data)
      })
  }
}
