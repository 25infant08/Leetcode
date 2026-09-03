class EventEmitter {
    subscribe(eventName, callback) {
        if (!this.events) this.events = new Map();
        if (!this.events.has(eventName)) {
            this.events.set(eventName, []);
        }
        const list = this.events.get(eventName);
        list.push(callback);
        return {
            unsubscribe: () => {
                const index = list.indexOf(callback);
                list.splice(index, 1);
            }
        };
    }
    emit(eventName, args = []) {
        if (!this.events || !this.events.has(eventName)) {
            return [];
        }
        return this.events.get(eventName).map(fn => fn(...args));
    }
}