import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-chiamata',
  templateUrl: './chiamata.component.html',
  styleUrls: ['./chiamata.component.css']
})
export class ChiamataComponent {

  cartaSearch !: String;
  obsCard !: Observable<any>;
  ris !: any;

  constructor(private http : HttpClient) {}

  ricercaApi() {
    
    this.obsCard = this.http.get<any>('https://5000-cantonirica-pythonmysql-l76v6qy4nm6.ws-eu107.gitpod.io/count')
    this.obsCard.subscribe(
      (data : any)=>
      {
        this.ris = (data);
        console.log(data)
      })
    
  }
  
}
