var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
const { convertFromDirectory } = require('joi-to-typescript');
function types() {
    return __awaiter(this, void 0, void 0, function* () {
        console.log('Running joi-to-typescript...');
        // Configure your settings here
        const result = yield convertFromDirectory({
            schemaDirectory: './src/validation',
            typeOutputDirectory: './src/interfaces',
            debug: true
        });
        if (result) {
            console.log('Completed joi-to-typescript');
        }
        else {
            console.log('Failed to run joi-to-typescript');
        }
    });
}
types();
