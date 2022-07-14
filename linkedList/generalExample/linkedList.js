

const LinkedList = () => ({
    size: 0,
    head: null
});


const Node = value => ({
    value,
    next: null
});


const myLL = new LinkedList();

myLL.head = new Node(5);
myLL.size = 1;

// {
//     size: 1,
//     head: {
//         value: 5,
//         next: null
//     }
// }

