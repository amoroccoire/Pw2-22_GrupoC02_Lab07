import { Component } from '@angular/core';
import { ApiService } from './api.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [ApiService]
})
export class AppComponent {
  title = 'cliente';

  products = [{nombre:'Producto',categoria:0,tipo:'Default', precio:0, disponible:true, imagen:'Default'}];

  constructor(private api:ApiService){
    this.getProducts();
  }

  getProducts = () => {
    this.api.getAllProducts().subscribe (
      data => {
        console.log(data);
        this.products = data;  //data.results;
      },
      error => {
        console.log(error);
      })  

    } 

}
