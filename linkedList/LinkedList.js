

export default LinkedList = () => ({
    size: 0,
    head: null
});


export const Node = value => ({
    value,
    next: null
});


export const DoubleReferenceNode = value => ({
    value,
    previous: null,
    next: null
});

