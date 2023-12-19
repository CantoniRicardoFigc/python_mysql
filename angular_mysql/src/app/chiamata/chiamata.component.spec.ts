import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ChiamataComponent } from './chiamata.component';

describe('ChiamataComponent', () => {
  let component: ChiamataComponent;
  let fixture: ComponentFixture<ChiamataComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ChiamataComponent]
    });
    fixture = TestBed.createComponent(ChiamataComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
