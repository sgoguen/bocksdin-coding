import LinkedList, { Node } from "../LinkedList";


const circularLinkedList = new LinkedList();


circularLinkedList.insert = function (value) {
    
    // instantiate a new node
    let newNode = new Node(value);

    // if the list is not empty, use the currentHead to set references
    if (circularLinkedList.head !== null) {
        
        // set newNode.next reference to existing head
        newNode.next = circularLinkedList.head;
        
        // find the last Node in the list to update its "next" reference
        let currentNode = circularLinkedList.head;
        while (currentNode !== null) {
            
            // if the next Node is the head, then we are at the end of the list
            if (currentNode.next === circularLinkedList.head) {
                
                // set the last Node in the list to reference the newNode
                currentNode.next = newNode;

                // break the loop
                break;
            }
            else {
                currentNode = currentNode.next;
            }
        }        

        // set head.next to reference the new node
        circularLinkedList.head.next = newNode;
    } 

    // if the list is empty
    else {
        // set newNode.next reference to newNode
        newNode.next = newNode;
    }

    // replace existing head reference with newNode reference
    circularLinkedList.head = newNode;

    // increase size value of linked list
    circularLinkedList.size++;
}


circularLinkedList.insert(5);
circularLinkedList.insert(2);
circularLinkedList.insert(10);

// {
//     "size": 3,
//     "head": {
//         "value": 10,
//         "next": {
//             "value": 2,
//             "next": {
//                 "value": 5,
//                 "next": {
//                     "value": 10,
//                     "next": { ... }
//                 }
//             }
//         }
//     }
// }


// assume circularLinkedList is a doubly linked list


circularLinkedList.insertAt = function (index, value) {

    // determine the midpoint of the linked list
    const midpoint = Math.floor(circularLinkedList.size / 2);

    // create a current index counter
    // if the index at which to insert is less than the midpoint, start at the beginning, else start at the end
        // use size instead of size - 1 because head can be seen as either 0 or size - 1 + 1
    let currentIndex = index < midpoint ? 0 : circularLinkedList.size;

    // create pointer variable
    // start with head of linked list
    let currentNode = circularLinkedList.head;
    while (currentNode !== null) {

        // determine next index
        let nextIndex = index < midpoint ? currentIndex + 1 : currentIndex - 1;
        
        // insert a new Node if the next currentIndex is the one for which we are searching
        if (nextIndex === index) {
            
            // create a new Node
            let newNode = new Node(value);

            // set newNode.next to reference the currentNode.next
            newNode.next = currentNode.next;

            // set currentNode.next to reference the newNode
            currentNode.next = newNode;

            // increase size value of linked list
            circularLinkedList.size++;

            // break the loop
            return;
        }
        else {
            // reference the next node in the list
            if (index < midpoint) {
                currentNode = currentNode.next;

                // increase the currentIndex value
                currentIndex++;
            }
            else {
                currentNode = currentNode.previous;

                // decrease the currentIndex value
                currentIndex--; 
            }
        }
    }
}


circularLinkedList.indexOf = function (value) {

    // create pointer variable
    // start with head of linked list
    let currentNode = circularLinkedList.head;

    // create a current index counter
    let currentIndex = 0;

    // while currentNode is not null, continue
    while (currentNode !== null) {

        // return the currentIndex if the currentNode.value is the one for which we are searching
        if (currentNode.value === value)
            return currentIndex;

        else {

            // reference the next node in the list
            currentNode = currentNode.next;

            // increment the currentIndex value
            currentIndex++;

        }

    }

    // if the value wasn't found, return -1
    return -1;
}


// can take in either a value or an index
// for the purpose of this demonstration we will look for a specific value
circularLinkedList.removeElement = function (value) {

    // create pointer variable
    // start with head of linked list
    let currentNode = circularLinkedList.head;

    // while currentNode is not null, continue
    while (currentNode !== null) {

        // if the currentNode.next is the node for which we are searching, remove it
        if (currentNode.next.value === value) {
            
            // set currentNode.next to reference the node-to-remove's next reference
            currentNode.next = currentNode.next.next;

            // decrease the size value of the linked list
            circularLinkedList.size--;

            // break the loop
            return;

        }

        else {

            // reference the next node in the list
            currentNode = currentNode.next;

        }

    }

}