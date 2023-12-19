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

  constructor(private http : HttpClient) {}

  ricercaGetAllData() {
    this.obsCard = this.http.get<Root>('https://5000-cantonirica-pythonmysql-l76v6qy4nm6.ws-eu107.gitpod.io/getAllDataInHtml')
    this.obsCard.subscribe(
      (data : Root)=>
      {
        this.ris = (data);
        console.log(data)
      })
  }

  ricercaCount() {
    this.obsCard1 = this.http.get<Root>('https://5000-cantonirica-pythonmysql-l76v6qy4nm6.ws-eu107.gitpod.io/count')
    this.obsCard1.subscribe(
      (data : Root)=>
      {
        this.ris1 = (data);
        console.log(data)
      })
  }
  
  
}
