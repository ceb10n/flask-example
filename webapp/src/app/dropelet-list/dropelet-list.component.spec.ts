import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DropeletListComponent } from './dropelet-list.component';

describe('DropeletListComponent', () => {
  let component: DropeletListComponent;
  let fixture: ComponentFixture<DropeletListComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DropeletListComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DropeletListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
