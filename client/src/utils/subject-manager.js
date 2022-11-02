import { Subject } from 'rxjs'

export class SubjectManager {
    subject$ = new Subject();

    getSubject() {
        return this.subject$.asObservable();
    }

    setSubject(value) {
        return this.subject$.next(value)
    }
}